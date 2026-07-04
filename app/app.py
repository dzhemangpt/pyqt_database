import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QStyledItemDelegate
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtCore import Qt, QDate, QTimer
from app.ui.new_main_ui import Ui_MainWindow


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
        self.db.setDatabaseName("sport_section.db")
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных sport_section.db")
            sys.exit(1)
        print("База данных подключена успешно!")

        # 2. Настройка моделей данных
        self.setup_models()

        # 3. Настройка интерфейса и связей
        self.setup_ui_logic()

        # 4. Заполнение ComboBox группами
        self.populate_comboboxes()

        # 5. Инициализация статистики
        self.update_statistics()

    def setup_models(self):
        # --- MODEL 1: Athletes (Спортсмены - верхняя таблица) ---
        self.model_athletes = QSqlTableModel(self, self.db)
        self.model_athletes.setTable("athletes")
        self.model_athletes.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model_athletes.setHeaderData(1, Qt.Orientation.Horizontal, "Имя атлета")
        self.model_athletes.setHeaderData(2, Qt.Orientation.Horizontal, "ID группы")
        self.model_athletes.setHeaderData(3, Qt.Orientation.Horizontal, "Дата рождения")
        self.model_athletes.setHeaderData(4, Qt.Orientation.Horizontal, "Рост")
        self.model_athletes.setHeaderData(5, Qt.Orientation.Horizontal, "Вес")
        self.model_athletes.select()
        self.tableView.setModel(self.model_athletes)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableView.setColumnHidden(0, True)

        # --- MODEL 2: Workouts (Тренировки - нижняя таблица) ---
        self.model_workouts = QSqlTableModel(self, self.db)
        self.model_workouts.setTable("workouts")
        self.model_workouts.setHeaderData(0, Qt.Orientation.Horizontal, "ID тренировки")
        self.model_workouts.setHeaderData(1, Qt.Orientation.Horizontal, "ID атлета")
        self.model_workouts.setHeaderData(2, Qt.Orientation.Horizontal, "Дата тренировки")
        self.model_workouts.setHeaderData(3, Qt.Orientation.Horizontal, "Время начала")
        self.model_workouts.setHeaderData(4, Qt.Orientation.Horizontal, "Длительность")
        self.model_workouts.setHeaderData(5, Qt.Orientation.Horizontal, "Тип тренировки")
        self.model_workouts.setHeaderData(6, Qt.Orientation.Horizontal, "Оценка")
        self.model_workouts.select()
        self.tableView_2.setModel(self.model_workouts)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableView_2.setColumnHidden(0, True)

    def populate_comboboxes(self):
        """Заполняем ComboBox группами из таблицы groups"""
        query = QSqlQuery("SELECT groud_id, group_name FROM groups ORDER BY groud_id", self.db)
        self.comboBox.clear()
        self.comboBox.addItem("Все группы", -1)
        while query.next():
            id_group = query.value(0)
            name_group = query.value(1)
            self.comboBox.addItem(name_group, id_group)

    def setup_ui_logic(self):
        # Связь: при клике на спортсмена показываем его тренировки
        self.tableView.selectionModel().selectionChanged.connect(self.on_athlete_selected)

        # Отслеживаем изменения в модели athletes для обновления статистики
        self.model_athletes.dataChanged.connect(self.on_athlete_data_changed)

        # === НОВОЕ: Отслеживаем изменения в модели workouts ===
        # Срабатывает при добавлении, удалении, изменении записей (включая поле mark)
        self.model_workouts.dataChanged.connect(self.on_workout_data_changed)
        # Также подключаем сигналы строк для отлова добавления/удаления
        self.model_workouts.rowsInserted.connect(self.on_workout_rows_changed)
        self.model_workouts.rowsRemoved.connect(self.on_workout_rows_changed)

        # Кнопки для athletes
        self.pushButton_3.clicked.connect(self.add_athlete)
        self.pushButton_4.clicked.connect(self.delete_athlete)
        self.pushButton_1.clicked.connect(self.search_athletes)
        self.pushButton_2.clicked.connect(self.clear_search)

        # Кнопки для workouts
        self.pushButton_5.clicked.connect(self.add_workout)
        self.pushButton_6.clicked.connect(self.delete_workout)

    # ================= ОБРАБОТЧИКИ ИЗМЕНЕНИЙ =================

    def on_athlete_data_changed(self, top_left, bottom_right, roles):
        """Вызывается при изменении данных в таблице athletes"""
        QTimer.singleShot(200, self.update_statistics)

    def on_workout_data_changed(self, top_left, bottom_right, roles):
        """Вызывается при изменении данных в таблице workouts (включая поле mark)"""
        QTimer.singleShot(200, self.update_statistics)

    def on_workout_rows_changed(self, parent, first, last):
        """Вызывается при добавлении или удалении строк в workouts"""
        QTimer.singleShot(200, self.update_statistics)

    # ================= СТАТИСТИКА =================

    def update_statistics(self, athlete_id=None):
        """Обновляет статистику для группы выбранного спортсмена"""
        if athlete_id is None:
            indexes = self.tableView.selectionModel().selectedRows()
            if indexes:
                row = indexes[0].row()
                athlete_id = self.model_athletes.data(self.model_athletes.index(row, 0))
            else:
                # Если ничего не выбрано – показываем нули
                self.label_9.setText("0")
                self.label_10.setText("0")
                return

        # Получаем group_id выбранного спортсмена (столбец с индексом 2)
        row = self.tableView.currentIndex().row()
        group_id = self.model_athletes.data(self.model_athletes.index(row, 2))

        if group_id is None:
            self.label_9.setText("0")
            self.label_10.setText("0")
            return

        # Считаем количество записей и среднее значение mark
        # для всех спортсменов из данной группы
        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT COUNT(w.mark), AVG(w.mark)
            FROM workouts w
            JOIN athletes a ON w.athlete_id = a.athlete_id
            WHERE a.group_id = :group_id
        """)
        query.bindValue(":group_id", group_id)
        query.exec()

        if query.next():
            count_marks = query.value(0) or 0
            avg_mark = query.value(1) or 0

            self.label_9.setText(str(count_marks))
            self.label_10.setText(f"{avg_mark:.2f}")
        else:
            self.label_9.setText("0")
            self.label_10.setText("0")

    # ================= ВЫБОР СТРОКИ =================

    def on_athlete_selected(self):
        """При выборе спортсмена фильтруем тренировки"""
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            # Если ничего не выбрано - показываем пустую таблицу
            self.model_workouts.setFilter("workout_id = -1")
            self.model_workouts.select()
            self.label_9.setText("0")
            self.label_10.setText("0")
            return

        # Получаем ID выбранного спортсмена (первый столбец = 0)
        row = indexes[0].row()
        athlete_id = self.model_athletes.data(self.model_athletes.index(row, 0))

        if athlete_id is not None:
            # Фильтруем тренировки по athlete_id
            self.model_workouts.setFilter(f"athlete_id = {athlete_id}")
            self.model_workouts.select()
            print(f"✓ Показаны тренировки для спортсмена ID={athlete_id}")
        else:
            self.model_workouts.setFilter("workout_id = -1")
            self.model_workouts.select()

        self.update_statistics()

    # ================= ДОБАВЛЕНИЕ / УДАЛЕНИЕ ATHLETES =================

    def add_athlete(self):
        """Добавление нового спортсмена"""
        row = self.model_athletes.rowCount()
        self.model_athletes.insertRow(row)
        self.tableView.selectRow(row)
        print(f"→ Добавлена новая строка спортсмена (row={row})")

    def delete_athlete(self):
        """Удаление спортсмена с подтверждением"""
        row = self.tableView.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Удалить спортсмена?")
        msg_box.setIcon(QMessageBox.Warning)
        btn_yes = msg_box.addButton("Да", QMessageBox.YesRole)
        btn_no = msg_box.addButton("Нет", QMessageBox.NoRole)
        msg_box.exec()

        if msg_box.clickedButton() == btn_yes:
            print(f"→ Попытка удаления спортсмена (row={row})")
            if self.model_athletes.removeRow(row):
                if self.model_athletes.submitAll():
                    print(f"  ✓ Спортсмен удален")
                    self.model_athletes.select()
                    self.update_statistics()
                    self.model_workouts.setFilter("workout_id = -1")
                    self.model_workouts.select()
                else:
                    print(f"  ✗ Ошибка сохранения: {self.model_athletes.lastError().text()}")
                    QMessageBox.critical(self, "Ошибка удаления",
                        f"Не удалось удалить запись.\n\nОшибка: {self.model_athletes.lastError().text()}")
                    self.model_athletes.select()
            else:
                print(f"  ✗ Не удалось удалить строку")
                QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку")

    # ================= ДОБАВЛЕНИЕ / УДАЛЕНИЕ WORKOUTS =================

    def add_workout(self):
        """Добавление тренировки с автоматическим заполнением athlete_id и даты"""
        indexes = self.tableView.selectionModel().selectedRows()
        athlete_id = None
        if indexes:
            athlete_id = self.model_athletes.data(self.model_athletes.index(indexes[0].row(), 0))

        if athlete_id is None:
            QMessageBox.warning(self, "Ошибка", "Выберите спортсмена для добавления тренировки")
            return

        row = self.model_workouts.rowCount()
        self.model_workouts.insertRow(row)

        # Автоматически заполняем athlete_id (столбец 1)
        idx_athlete = self.model_workouts.index(row, 1)
        self.model_workouts.setData(idx_athlete, athlete_id)

        # Автоматически заполняем date1 (столбец 2) текущей датой
        idx_date = self.model_workouts.index(row, 2)
        self.model_workouts.setData(idx_date, QDate.currentDate().toString("yyyy-MM-dd"))

        # Автоматически заполняем start_time (столбец 3) текущим временем
        idx_time = self.model_workouts.index(row, 3)
        now = datetime.now()
        self.model_workouts.setData(idx_time, now.strftime("%H:%M"))

        self.tableView_2.selectRow(row)
        print(f"→ Добавлена новая тренировка для спортсмена ID={athlete_id}")

    def delete_workout(self):
        """Удаление тренировки с подтверждением"""
        row = self.tableView_2.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Удалить тренировку?")
        msg_box.setIcon(QMessageBox.Warning)
        btn_yes = msg_box.addButton("Да", QMessageBox.YesRole)
        btn_no = msg_box.addButton("Нет", QMessageBox.NoRole)
        msg_box.exec()

        if msg_box.clickedButton() == btn_yes:
            print(f"→ Попытка удаления тренировки (row={row})")
            if self.model_workouts.removeRow(row):
                if self.model_workouts.submitAll():
                    print(f"  ✓ Тренировка удалена")
                    self.model_workouts.select()
                    # Статистика обновится через сигнал rowsRemoved
                else:
                    print(f"  ✗ Ошибка сохранения: {self.model_workouts.lastError().text()}")
                    QMessageBox.critical(self, "Ошибка удаления",
                        f"Не удалось удалить тренировку.\n\nОшибка: {self.model_workouts.lastError().text()}")
                    self.model_workouts.select()
            else:
                print(f"  ✗ Не удалось удалить строку")
                QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку")

    # ================= ПОИСК (нечувствительный к регистру) =================

    def search_athletes(self):
        """Поиск спортсменов с фильтрацией на стороне Python (нечувствителен к регистру)"""
        name = self.lineEdit_3.text().strip().lower()
        group_idx = self.comboBox.currentIndex()
        group_id = self.comboBox.itemData(group_idx)
        date_from = self.lineEdit_4.text().strip()
        date_to = self.lineEdit_2.text().strip()

        # Получаем все данные из таблицы athletes
        query = QSqlQuery("SELECT * FROM athletes", self.db)

        filtered_ids = []
        while query.next():
            athlete_id = query.value(0)
            name_val = (query.value(1) or "").lower()
            group_val = query.value(2)
            birth_date = query.value(3) or ""

            match = True

            # Фильтр по имени (нечувствителен к регистру)
            if name and name not in name_val:
                match = False

            # Фильтр по группе
            if group_id != -1 and group_val != group_id:
                match = False

            # Фильтр по дате рождения (от)
            if date_from and birth_date < date_from:
                match = False

            # Фильтр по дате рождения (до)
            if date_to and birth_date > date_to:
                match = False

            if match:
                filtered_ids.append(str(athlete_id))

        # Применяем фильтр
        if filtered_ids:
            ids_str = ",".join(filtered_ids)
            self.model_athletes.setFilter(f"athlete_id IN ({ids_str})")
        else:
            self.model_athletes.setFilter("athlete_id = -1")

        self.model_athletes.select()
        print(f"🔍 Найдено спортсменов: {len(filtered_ids)}")

    def clear_search(self):
        """Сброс всех фильтров поиска"""
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.comboBox.setCurrentIndex(0)
        self.model_athletes.setFilter("")
        self.model_athletes.select()
        print("🔄 Поиск сброшен")

    def closeEvent(self, event):
        """При закрытии приложения сохраняем все изменения"""
        self.model_athletes.submitAll()
        self.model_workouts.submitAll()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppLogic()
    window.show()
    sys.exit(app.exec())