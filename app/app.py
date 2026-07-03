import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QStyledItemDelegate
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import Qt, QDate
from app.ui.new_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QDate, QTimer
from PySide6.QtSql import QSqlQueryModel
class NumberDelegate(QStyledItemDelegate):
    """Делегат для форматирования чисел (цена с 2 знаками после запятой)"""
    def displayText(self, value, locale):
        if isinstance(value, (int, float)):
            if value == int(value):
                return str(int(value))
            else:
                return f"{value:.2f}"
        return str(value)

class AppLogic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 1. Подключение к базе данных
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("toys.db")
        
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных toys.db")
            sys.exit(1)
        
        print("База данных подключена успешно!")

        # 2. Настройка моделей данных
        self.setup_models()
        
        # 3. Настройка интерфейса и связей
        self.setup_ui_logic()
        
        # 4. Заполнение ComboBox категориями
        self.populate_comboboxes()
        
        # 5. Инициализация статистики
        self.update_statistics()

    def setup_models(self):
        # --- MODEL 1: Toys (Игрушки - верхняя таблица) ---
        self.model_toys = QSqlTableModel(self, self.db)
        self.model_toys.setTable("toys")
        self.model_toys.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model_toys.setHeaderData(1, Qt.Orientation.Horizontal, "Название")
        self.model_toys.setHeaderData(2, Qt.Orientation.Horizontal, "ID Категории")
        self.model_toys.setHeaderData(3, Qt.Orientation.Horizontal, "Производитель")
        self.model_toys.setHeaderData(4, Qt.Orientation.Horizontal, "Цена")
        self.model_toys.setHeaderData(5, Qt.Orientation.Horizontal, "Возраст")
        self.model_toys.setHeaderData(6, Qt.Orientation.Horizontal, "Количество")
        self.model_toys.setHeaderData(7, Qt.Orientation.Horizontal, "Описание")
        self.model_toys.select()
        self.tableView.setModel(self.model_toys)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        
        # Устанавливаем делегат для столбца "Цена" (индекс 4)
        price_delegate = NumberDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(4, price_delegate)

        # --- MODEL 2: Reviews (Отзывы - нижняя таблица) ---
        self.model_reviews = QSqlTableModel(self, self.db)
        self.model_reviews.setTable("reviews")
        self.model_reviews.setHeaderData(0, Qt.Orientation.Horizontal, "ID Отзыва")
        # Скрываем id_toy (индекс 1), не устанавливаем заголовок
        self.model_reviews.setHeaderData(2, Qt.Orientation.Horizontal, "Имя покупателя")
        self.model_reviews.setHeaderData(3, Qt.Orientation.Horizontal, "Рейтинг")
        self.model_reviews.setHeaderData(4, Qt.Orientation.Horizontal, "Текст")
        self.model_reviews.setHeaderData(5, Qt.Orientation.Horizontal, "Дата покупки")
        self.model_reviews.setHeaderData(6, Qt.Orientation.Horizontal, "Дата отзыва")
        self.model_reviews.select()
        self.tableView_2.setModel(self.model_reviews)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        
        # Скрываем столбец id_toy (индекс 1)
        self.tableView_2.setColumnHidden(1, True)

    def populate_comboboxes(self):
        """Заполняем ComboBox категориями из таблицы category"""
        query = QSqlQuery("SELECT id_category, title_category FROM category ORDER BY title_category", self.db)
        self.comboBox.clear()
        self.comboBox.addItem("Все категории", -1)  # Значение -1 для отображения всех
        
        while query.next():
            id_category = query.value(0)
            title_category = query.value(1)
            self.comboBox.addItem(title_category, id_category)

    def setup_ui_logic(self):
    # Связь: при клике на игрушку показываем её отзывы
        self.tableView.selectionModel().selectionChanged.connect(self.on_toy_selected)
        
        # Отслеживаем изменения в модели toys для обновления статистики
        self.model_toys.dataChanged.connect(self.on_toy_modified)
        
        # Кнопки для toys
        self.pushButton_3.clicked.connect(self.add_toy)
        self.pushButton_4.clicked.connect(self.delete_toy)
        self.pushButton_1.clicked.connect(self.search_toys)
        self.pushButton_2.clicked.connect(self.reset_search)
        
        # Кнопки для reviews
        self.pushButton_5.clicked.connect(self.add_review)
        self.pushButton_6.clicked.connect(self.delete_review)

    def on_toy_modified(self, top_left, bottom_right, roles):
        """Вызывается при изменении данных в таблице toys"""
        # Используем QTimer для отложенного вызова после сохранения в БД
        QTimer.singleShot(200, self.update_statistics)

    def on_toy_selected(self):
        """При выборе игрушки фильтруем отзывы"""
        indexes = self.tableView.selectionModel().selectedRows()
        
        if not indexes:
            # Если ничего не выбрано - показываем пустую таблицу
            self.model_reviews.setFilter("id_review = -1")
            self.model_reviews.select()
            return
        
        # Получаем ID выбранной игрушки (первый столбец = 0)
        row = indexes[0].row()
        toy_id = self.model_toys.data(self.model_toys.index(row, 0))
        
        if toy_id is not None:
            # Фильтруем отзывы по id_toy
            self.model_reviews.setFilter(f"id_toy = {toy_id}")
            self.model_reviews.select()
            print(f"✓ Показаны отзывы для игрушки ID={toy_id}")
        else:
            self.model_reviews.setFilter("id_review = -1")
            self.model_reviews.select()

    def add_toy(self):
        """Добавление новой игрушки"""
        row = self.model_toys.rowCount()
        self.model_toys.insertRow(row)
        self.tableView.selectRow(row)
        print(f"→ Добавлена новая строка игрушки (row={row})")

    def delete_toy(self):
        """Удаление игрушки с подтверждением"""
        row = self.tableView.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return
        
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Удалить игрушку?")
        msg_box.setIcon(QMessageBox.Warning)
        btn_yes = msg_box.addButton("Да", QMessageBox.YesRole)
        btn_no = msg_box.addButton("Нет", QMessageBox.NoRole)
        msg_box.exec()
        
        if msg_box.clickedButton() == btn_yes:
            print(f"→ Попытка удаления игрушки (row={row})")
            if self.model_toys.removeRow(row):
                if self.model_toys.submitAll():
                    print(f"  ✓ Игрушка удалена")
                    # ОБЯЗАТЕЛЬНО обновляем модель после удаления
                    self.model_toys.select()
                    # Обновляем статистику после удаления
                    self.update_statistics()
                    # Если был выбран удаленный элемент, очищаем отзывы
                    self.model_reviews.setFilter("id_review = -1")
                    self.model_reviews.select()
                else:
                    print(f"  ✗ Ошибка сохранения: {self.model_toys.lastError().text()}")
                    QMessageBox.critical(self, "Ошибка удаления", 
                        f"Не удалось удалить запись.\n\nОшибка: {self.model_toys.lastError().text()}")
                    self.model_toys.select()
            else:
                print(f"  ✗ Не удалось удалить строку")
                QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку")

    def add_review(self):
        """Добавление отзыва с автоматическим заполнением id_toy и date_review"""
        # Получаем выбранную игрушку
        indexes = self.tableView.selectionModel().selectedRows()
        toy_id = None
        if indexes:
            toy_id = self.model_toys.data(self.model_toys.index(indexes[0].row(), 0))
        
        if toy_id is None:
            QMessageBox.warning(self, "Ошибка", "Выберите игрушку для добавления отзыва")
            return
        
        row = self.model_reviews.rowCount()
        self.model_reviews.insertRow(row)
        
        # Автоматически заполняем id_toy (столбец 1)
        idx_toy = self.model_reviews.index(row, 1)
        self.model_reviews.setData(idx_toy, toy_id)
        
        # Автоматически заполняем date_review (столбец 6) текущей датой
        idx_date = self.model_reviews.index(row, 6)
        self.model_reviews.setData(idx_date, QDate.currentDate().toString("yyyy-MM-dd"))
        
        self.tableView_2.selectRow(row)
        print(f"→ Добавлен новый отзыв для игрушки ID={toy_id}")

    def delete_review(self):
        """Удаление отзыва с подтверждением"""
        row = self.tableView_2.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return
        
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Удалить отзыв?")
        msg_box.setIcon(QMessageBox.Warning)
        btn_yes = msg_box.addButton("Да", QMessageBox.YesRole)
        btn_no = msg_box.addButton("Нет", QMessageBox.NoRole)
        msg_box.exec()
        
        if msg_box.clickedButton() == btn_yes:
            print(f"→ Попытка удаления отзыва (row={row})")
            if self.model_reviews.removeRow(row):
                if self.model_reviews.submitAll():
                    print(f"  ✓ Отзыв удален")
                    # ОБЯЗАТЕЛЬНО обновляем модель после удаления
                    self.model_reviews.select()
                else:
                    print(f"  ✗ Ошибка сохранения: {self.model_reviews.lastError().text()}")
                    QMessageBox.critical(self, "Ошибка удаления", 
                        f"Не удалось удалить отзыв.\n\nОшибка: {self.model_reviews.lastError().text()}")
                    self.model_reviews.select()
            else:
                print(f"  ✗ Не удалось удалить строку")
                QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку")

    def search_toys(self):
        """Поиск игрушек с фильтрацией на стороне Python для поддержки кириллицы"""
        title_toy = self.lineEdit_2.text().lower()
        category_index = self.comboBox.currentIndex()
        category_id = self.comboBox.itemData(category_index)
        maker = self.lineEdit_3.text().lower()
        description = self.lineEdit_4.text().lower()
        cost_from = self.spinBox_1.value()
        cost_to = self.spinBox_2.value()
        count_from = self.spinBox_3.value()
        count_to = self.spinBox_4.value()
        
        # Получаем все данные из таблицы toys
        query = QSqlQuery("SELECT * FROM toys", self.db)
        
        # Создаем временную модель для отфильтрованных результатов
        filtered_model = QSqlQueryModel(self)
        
        # Собираем отфильтрованные данные
        filtered_data = []
        while query.next():
            id_toy = query.value(0)
            title = query.value(1) or ""
            id_category = query.value(2)
            maker_val = query.value(3) or ""
            cost = query.value(4) or 0
            age = query.value(5)
            count = query.value(6) or 0
            desc = query.value(7) or ""
            
            # Проверяем условия (регистронезависимо)
            match = True
            
            if title_toy and title_toy not in title.lower():
                match = False
            if category_id != -1 and id_category != category_id:
                match = False
            if maker and maker not in maker_val.lower():
                match = False
            if description and description not in desc.lower():
                match = False
            if cost_from > 0 and cost < cost_from:
                match = False
            if cost_to > 0 and cost > cost_to:
                match = False
            if count_from > 0 and count < count_from:
                match = False
            if count_to > 0 and count > count_to:
                match = False
            
            if match:
                filtered_data.append((id_toy, title, id_category, maker_val, cost, age, count, desc))
        
        # Если есть результаты, показываем их
        if filtered_data:
            # Создаем SQL запрос с ID найденных записей
            ids = [str(d[0]) for d in filtered_data]
            ids_str = ",".join(ids)
            self.model_toys.setFilter(f"id_toy IN ({ids_str})")
        else:
            # Если ничего не найдено, показываем пустую таблицу
            self.model_toys.setFilter("id_toy = -1")
        
        self.model_toys.select()
        print(f"🔍 Найдено записей: {len(filtered_data)}")

    def update_statistics(self):
        """Обновление статистики из таблицы toys_statistics"""
        query = QSqlQuery("SELECT count_toys, min_cost, max_cost, avg_cost FROM toys_statistics WHERE id=1", self.db)
        
        if query.next():
            count_toys = query.value(0) or 0
            min_cost = query.value(1) or 0
            max_cost = query.value(2) or 0
            avg_cost = query.value(3) or 0
            
            # Обновляем labels
            self.label_9.setText(str(count_toys))
            self.label_10.setText(str(min_cost))
            self.label_11.setText(str(max_cost))
            # avg_cost с 2 знаками после запятой
            self.label_12.setText(f"{avg_cost:.2f}")
            
            print(f"📊 Статистика обновлена: count={count_toys}, min={min_cost}, max={max_cost}, avg={avg_cost:.2f}")
        else:
            # Если данных нет, устанавливаем нули
            self.label_9.setText("0")
            self.label_10.setText("0")
            self.label_11.setText("0")
            self.label_12.setText("0.00")
            print("⚠️ Таблица toys_statistics пуста")

    def closeEvent(self, event):
        """При закрытии приложения сохраняем все изменения"""
        # Принудительно сохраняем все изменения в БД
        self.model_toys.submitAll()
        self.model_reviews.submitAll()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppLogic()
    window.show()
    sys.exit(app.exec())