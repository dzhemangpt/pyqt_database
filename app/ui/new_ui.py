# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableView,
    QWidget)
import app.ui.icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 519)
        MainWindow.setMinimumSize(QSize(947, 519))
        MainWindow.setMaximumSize(QSize(947, 519))
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.221591, stop:0 rgba(194, 0, 90, 255), stop:0.994318 rgba(255, 164, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.79, y1:1, x2:0.705, y2:0.0625, stop:0 rgba(48, 0, 173, 255), stop:1 rgba(255, 3, 255, 255));\n"
"font-family: Noto Sans SC;")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 951, 521))
        self.tabWidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.79, y1:1, x2:0.705, y2:0.0625, stop:0 rgba(48, 0, 173, 255), stop:1 rgba(255, 3, 255, 255));\n"
"")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tableView = QTableView(self.tab1)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 711, 241))
        self.tableView.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(730, 10, 211, 431))
        self.groupBox.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border-radius: 7px;\n"
"border: 1px solid rgb(255,255,255);\n"
"")
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 30, 181, 31))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 110, 181, 31))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 150, 181, 31))
        self.pushButton_1 = QPushButton(self.groupBox)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 370, 81, 41))
        self.pushButton_1.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/search_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QSize(16, 16))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 370, 91, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/close_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(16, 16))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 70, 181, 31))
        self.comboBox.setEditable(False)
        self.label_1 = QLabel(self.groupBox)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 195, 81, 21))
        self.label_1.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.spinBox_1 = QSpinBox(self.groupBox)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(100, 190, 101, 31))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 230, 81, 21))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(100, 225, 101, 31))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 275, 91, 21))
        self.label_3.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 310, 91, 21))
        self.label_4.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(120, 305, 81, 31))
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(120, 270, 81, 31))
        self.pushButton_4 = QPushButton(self.tab1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(510, 260, 181, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/delete_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(16, 16))
        self.pushButton_3 = QPushButton(self.tab1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 260, 181, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/add_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(16, 16))
        self.tableView_2 = QTableView(self.tab1)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(10, 300, 711, 101))
        self.tableView_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pushButton_5 = QPushButton(self.tab1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(300, 410, 181, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_6 = QPushButton(self.tab1)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(510, 410, 181, 31))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"font: 75 14pt \"Calibri\";\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60);\n"
"}")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(16, 16))
        self.label_5 = QLabel(self.tab1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 410, 151, 16))
        self.label_5.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_6 = QLabel(self.tab1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 430, 151, 16))
        self.label_6.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_7 = QLabel(self.tab1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 450, 151, 16))
        self.label_7.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_8 = QLabel(self.tab1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 470, 151, 16))
        self.label_8.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_9 = QLabel(self.tab1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 410, 91, 16))
        self.label_9.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_10 = QLabel(self.tab1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 430, 91, 16))
        self.label_10.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_11 = QLabel(self.tab1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(170, 450, 91, 16))
        self.label_11.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.label_12 = QLabel(self.tab1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(170, 470, 91, 16))
        self.label_12.setStyleSheet(u"font: 75 12pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.tabWidget.addTab(self.tab1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_1)
        QWidget.setTabOrder(self.pushButton_1, self.tableView)
        QWidget.setTabOrder(self.tableView, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableView_2)
        QWidget.setTabOrder(self.tableView_2, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u0443\u0448\u043a\u0438", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043e\u0442:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0434\u043e:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043e\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0434\u043e:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0446\u0435\u043d\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u044b", None))
    # retranslateUi