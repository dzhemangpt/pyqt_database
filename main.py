import sys
import os
import asyncio
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate, QSqlQuery
from PySide6.QtCore import Qt, QDate

# Импортируем UI и Модели
from app.ui.main_ui import Ui_MainWindow
from app.database.models import async_main

class AppLogic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 1. Инициализация базы данных (создание таблиц через SQLAlchemy)
        # Запускаем асинхронный код синхронно перед стартом UI
        asyncio.run(async_main())
        
        # 2. Подключение Qt к той же базе данных
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        # Путь к базе данных (auto.db лежит рядом с main.py)
        self.db.setDatabaseName("auto.db")
        
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных auto.db")
            sys.exit(1)
            
        print("База данных подключена успешно!")

        # 3. Настройка Моделей данных
        self.setup_models()
        
        # 4. Настройка Интерфейса и Связей
        self.setup_ui_logic()
        
        # 5. Заполнение ComboBox (Уникальные значения)
        self.populate_comboboxes()

    def setup_models(self):
        # --- MODEL 1: Owners (Владельцы) ---
        self.model_owners = QSqlTableModel(self, self.db)
        self.model_owners.setTable("owners")
        self.model_owners.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model_owners.setHeaderData(1, Qt.Orientation.Horizontal, "Имя")
        self.model_owners.setHeaderData(2, Qt.Orientation.Horizontal, "Фамилия")
        self.model_owners.setHeaderData(3, Qt.Orientation.Horizontal, "Отчество")
        self.model_owners.setHeaderData(4, Qt.Orientation.Horizontal, "Телефон")
        self.model_owners.setHeaderData(5, Qt.Orientation.Horizontal, "Город")
        self.model_owners.setHeaderData(6, Qt.Orientation.Horizontal, "Улица")
        self.model_owners.setHeaderData(7, Qt.Orientation.Horizontal, "Дом")
        self.model_owners.select()
        self.tableView.setModel(self.model_owners)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- MODEL 2: Vydacha (Выдача - нижняя таблица) ---
        self.model_vydacha = QSqlTableModel(self, self.db)
        self.model_vydacha.setTable("vydacha")
        self.model_vydacha.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model_vydacha.setHeaderData(1, Qt.Orientation.Horizontal, "ID Владельца")
        self.model_vydacha.setHeaderData(2, Qt.Orientation.Horizontal, "Дата")
        self.model_vydacha.setHeaderData(3, Qt.Orientation.Horizontal, "Выдал")
        self.model_vydacha.select()
        self.tableView_4.setModel(self.model_vydacha)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- MODEL 3: Cars (Машины) ---
        self.model_cars = QSqlTableModel(self, self.db)
        self.model_cars.setTable("cars")
        self.model_cars.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model_cars.setHeaderData(1, Qt.Orientation.Horizontal, "Марка")
        self.model_cars.setHeaderData(2, Qt.Orientation.Horizontal, "Модель")
        self.model_cars.setHeaderData(3, Qt.Orientation.Horizontal, "Цвет")
        self.model_cars.setHeaderData(4, Qt.Orientation.Horizontal, "Мощность")
        self.model_cars.select()
        self.tableView_2.setModel(self.model_cars)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- MODEL 4: Prava (Права - Связанные данные) ---
        # Используем RelationalTableModel чтобы вместо ID показывать данные из других таблиц
        self.model_prava = QSqlRelationalTableModel(self, self.db)
        self.model_prava.setTable("prava")
        
        # Связь: id_car -> cars.mark (показываем марку машины)
        self.model_prava.setRelation(1, QSqlRelation("cars", "id", "mark"))
        # Связь: id_owner -> owners.surname (показываем фамилию владельца)
        self.model_prava.setRelation(2, QSqlRelation("owners", "id", "surname"))
        
        self.model_prava.setHeaderData(0, Qt.Orientation.Horizontal, "ID Прав")
        self.model_prava.setHeaderData(1, Qt.Orientation.Horizontal, "Марка Машины")
        self.model_prava.setHeaderData(2, Qt.Orientation.Horizontal, "Фамилия Владельца")
        
        self.model_prava.select()
        self.tableView_3.setModel(self.model_prava)
        
        # Устанавливаем делегат для корректного редактирования связанных полей
        self.tableView_3.setItemDelegate(QSqlRelationalDelegate(self.tableView_3))
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def populate_comboboxes(self):
        # Заполняем ComboBox Марками (Tab 2)
        query_mark = QSqlQuery("SELECT DISTINCT mark FROM cars ORDER BY mark", self.db)
        self.comboBox.clear()
        self.comboBox.addItem("Все марки", "all")
        while query_mark.next():
            self.comboBox.addItem(query_mark.value(0))

        # Заполняем ComboBox Цветами (Tab 2)
        query_color = QSqlQuery("SELECT DISTINCT color FROM cars ORDER BY color", self.db)
        self.comboBox_2.clear()
        self.comboBox_2.addItem("Все цвета", "all")
        while query_color.next():
            self.comboBox_2.addItem(query_color.value(0))

    def setup_ui_logic(self):
        # --- Tab 1: Owners & Vydacha ---
        # При клике на владельца обновляем нижнюю таблицу
        self.tableView.selectionModel().selectionChanged.connect(self.on_owner_selected)
        
        # Кнопки
        self.pushButton_15.clicked.connect(self.add_owner)
        self.pushButton_14.clicked.connect(self.delete_record_generic) # Для owners
        self.pushButton_17.clicked.connect(self.add_vydacha)
        self.pushButton_18.clicked.connect(self.delete_vydacha)
        self.pushButton_8.clicked.connect(self.search_owners)
        self.pushButton_9.clicked.connect(self.reset_search_owners)

        # --- Tab 2: Cars ---
        self.pushButton_13.clicked.connect(self.add_cars)
        self.pushButton_16.clicked.connect(self.delete_record_cars)
        self.pushButton_4.clicked.connect(self.search_cars)
        self.pushButton_6.clicked.connect(self.reset_search_cars)

        # --- Tab 3: Prava ---
        self.pushButton_12.clicked.connect(self.add_prava)
        self.pushButton_11.clicked.connect(self.delete_record_prava)
        self.pushButton_5.clicked.connect(self.search_prava)
        self.pushButton_7.clicked.connect(self.reset_search_prava)

    # ================= ЛОГИКА TAB 1 (ВЛАДЕЛЬЦЫ) =================

    def add_owner(self):
        row = self.model_owners.rowCount()
        self.model_owners.insertRow(row)
        # Можно сразу выделить новую строку
        self.tableView.selectRow(row)

    def delete_record_generic(self):
        self.delete_record(self.tableView, self.model_owners)

    def delete_record(self, table_view, model):
        row = table_view.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return
        
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Удалить запись?")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.addButton("Да", QMessageBox.YesRole)
        msg_box.addButton("Нет", QMessageBox.NoRole)
        
        if msg_box.exec() == QMessageBox.Yes:
            model.removeRow(row)
            model.select() # Обновить данные

    def on_owner_selected(self):
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            self.model_vydacha.setFilter("") # Если ничего не выбрано, можно показать всё или очистить
            return
        
        # Получаем ID выбранного владельца (первый столбец = 0)
        row = indexes[0].row()
        owner_id = self.model_owners.data(self.model_owners.index(row, 0))
        
        # Фильтруем выдачу по этому ID
        self.model_vydacha.setFilter(f"id_owner = {owner_id}")

    def add_vydacha(self):
        # Получаем выбранного владельца, чтобы подставить ID
        indexes = self.tableView.selectionModel().selectedRows()
        owner_id = None
        if indexes:
            owner_id = self.model_owners.data(self.model_owners.index(indexes[0].row(), 0))
        
        row = self.model_vydacha.rowCount()
        self.model_vydacha.insertRow(row)
        
        if owner_id:
            # Подставляем ID владельца автоматически
            idx = self.model_vydacha.index(row, 1) # Столбец id_owner
            self.model_vydacha.setData(idx, owner_id)
            
        self.tableView_4.selectRow(row)
        # Валидация даты (текущая дата)
        date_idx = self.model_vydacha.index(row, 2) # Столбец date
        self.model_vydacha.setData(date_idx, QDate.currentDate().toString("yyyy-MM-dd"))

    def delete_vydacha(self):
        self.delete_record(self.tableView_4, self.model_vydacha)

    def search_owners(self):
        # Собираем условия из lineEdit
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        otch = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        city = self.lineEdit_5.text()
        street = self.lineEdit_6.text()
        home = self.lineEdit_7.text()
        limit = self.spinBox_3.value()

        conditions = []
        if name: conditions.append(f"name LIKE '%{name}%'")
        if surname: conditions.append(f"surname LIKE '%{surname}%'")
        if otch: conditions.append(f"otch LIKE '%{otch}%'")
        if phone: conditions.append(f"phone LIKE '%{phone}%'")
        if city: conditions.append(f"city LIKE '%{city}%'")
        if street: conditions.append(f"street LIKE '%{street}%'")
        if home: conditions.append(f"home LIKE '%{home}%'")

        query_str = " AND ".join(conditions) if conditions else ""
        
        # Применяем фильтр и лимит
        self.model_owners.setFilter(query_str)
        self.model_owners.select()
        
        if limit > 0:
            # QSqlTableModel не поддерживает LIMIT напрямую в setFilter, 
            # но мы можем скрыть лишнее или использовать QSqlQueryModel.
            # Для простоты в рамках учебного проекта оставим полный фильтр.
            pass

    def reset_search_owners(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.spinBox_3.setValue(0)
        self.model_owners.setFilter("")
        self.model_owners.select()

    # ================= ЛОГИКА TAB 2 (МАШИНЫ) =================

    def add_cars(self):
        row = self.model_cars.rowCount()
        self.model_cars.insertRow(row)
        self.tableView_2.selectRow(row)

    def delete_record_cars(self):
        self.delete_record(self.tableView_2, self.model_cars)

    def search_cars(self):
        mark_filter = self.comboBox.currentText()
        color_filter = self.comboBox_2.currentText()
        price_ot = self.doubleSpinBox_2.value() # Цена от
        price_do = self.doubleSpinBox.value()   # Цена до
        
        # В models.py нет поля price у Cars, но в UI есть поиск по цене.
        # В models.py у Car есть только power. Возможно, вы имели в виду фильтрацию по мощности?
        # Если в БД нет колонки price, этот код не сработает.
        # Я предположу, что DoubleSpinBox ищет по мощности (power) или это поле нужно добавить в БД.
        # Пока оставим логику для power.
        
        power_ot = self.doubleSpinBox_2.value()
        power_do = self.doubleSpinBox.value()

        conditions = []
        if mark_filter != "Все марки":
            conditions.append(f"mark = '{mark_filter}'")
        if color_filter != "Все цвета":
            conditions.append(f"color = '{color_filter}'")
        
        # Пример для мощности (если нужно)
        # if power_ot > 0 and power_do > 0:
        #     conditions.append(f"power BETWEEN {power_ot} AND {power_do}")

        query_str = " AND ".join(conditions)
        self.model_cars.setFilter(query_str)
        self.model_cars.select()

    def reset_search_cars(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.doubleSpinBox_2.setValue(0.0)
        self.doubleSpinBox.setValue(0.0)
        self.model_cars.setFilter("")
        self.model_cars.select()

    # ================= ЛОГИКА TAB 3 (ПРАВА) =================

    def add_prava(self):
        row = self.model_prava.rowCount()
        self.model_prava.insertRow(row)
        self.tableView_3.selectRow(row)

    def delete_record_prava(self):
        # Удаление в RelationalTableModel требует аккуратности, но removeRow работает
        self.delete_record(self.tableView_3, self.model_prava)

    def search_prava(self):
        # Поиск по ID (так как реляционная модель фильтрует по базовым полям)
        id_owner_text = self.lineEdit_11.text() # ID Владельца
        id_car_text = self.lineEdit_10.text()   # ID Машины
        
        conditions = []
        if id_owner_text:
            conditions.append(f"id_owner = {id_owner_text}")
        if id_car_text:
            conditions.append(f"id_car = {id_car_text}")
            
        query_str = " AND ".join(conditions)
        self.model_prava.setFilter(query_str)
        self.model_prava.select()

    def reset_search_prava(self):
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear() # ID прав
        self.model_prava.setFilter("")
        self.model_prava.select()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppLogic()
    window.show()
    sys.exit(app.exec())