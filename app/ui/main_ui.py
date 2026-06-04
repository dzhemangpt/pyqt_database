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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableView, QWidget)
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
        self.tableView.setGeometry(QRect(10, 10, 711, 251))
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
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 70, 181, 31))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 310, 181, 16))
        self.label.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 7px;")
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 30, 181, 31))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 110, 181, 31))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 150, 181, 31))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 190, 181, 31))
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 230, 181, 31))
        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 270, 181, 31))
        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 370, 81, 41))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(16, 16))
        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(110, 370, 91, 41))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(16, 16))
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(20, 330, 181, 31))
        self.pushButton_14 = QPushButton(self.tab1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(510, 270, 181, 31))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(16, 16))
        self.pushButton_15 = QPushButton(self.tab1)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(300, 270, 181, 31))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.tableView_4 = QTableView(self.tab1)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setGeometry(QRect(10, 310, 711, 141))
        self.tableView_4.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pushButton_17 = QPushButton(self.tab1)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(300, 460, 181, 31))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_17.setIcon(icon3)
        self.pushButton_17.setIconSize(QSize(16, 16))
        self.pushButton_18 = QPushButton(self.tab1)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(510, 460, 181, 31))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QSize(16, 16))
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tableView_2 = QTableView(self.tab2)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(20, 10, 441, 431))
        self.tableView_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.groupBox_2 = QGroupBox(self.tab2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 10, 211, 431))
        self.groupBox_2.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(20, 60, 181, 31))
        self.lineEdit_8.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 290, 181, 16))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 0px;")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 370, 81, 41))
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
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(16, 16))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 181, 31))
        self.comboBox.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;\n"
"color:white;")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 110, 181, 31))
        self.comboBox_2.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 150, 91, 16))
        self.label_3.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 0px;")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 210, 81, 16))
        self.label_4.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 0px;")
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(110, 370, 91, 41))
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
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(16, 16))
        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(20, 310, 181, 31))
        self.spinBox.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(20, 230, 181, 31))
        self.doubleSpinBox.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.doubleSpinBox.setMaximum(1000000000.000000000000000)
        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(20, 170, 181, 31))
        self.doubleSpinBox_2.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.doubleSpinBox_2.setMaximum(1000000000.000000000000000)
        self.pushButton_13 = QPushButton(self.tab2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(210, 450, 181, 31))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setIconSize(QSize(16, 16))
        self.pushButton_16 = QPushButton(self.tab2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(400, 450, 181, 31))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setIconSize(QSize(16, 16))
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.groupBox_3 = QGroupBox(self.tab3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(510, 10, 211, 431))
        self.groupBox_3.setStyleSheet(u"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 1px solid rgb(255,255,255);\n"
"border-radius: 7px;")
        self.lineEdit_10 = QLineEdit(self.groupBox_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(20, 40, 181, 31))
        self.lineEdit_11 = QLineEdit(self.groupBox_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(20, 90, 181, 31))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 181, 21))
        self.label_5.setStyleSheet(u"font-color:white;\n"
"font: 75 16pt \"Calibri\";\n"
"background-color:rgba(255,255,255,0);\n"
"color:white;\n"
"border: 0px solid rgba(255,255,255);\n"
"border-radius: 0px;")
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 270, 81, 41))
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
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(110, 270, 91, 41))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.spinBox_2 = QSpinBox(self.groupBox_3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(20, 200, 181, 31))
        self.tableView_3 = QTableView(self.tab3)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(10, 10, 491, 431))
        self.tableView_3.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pushButton_11 = QPushButton(self.tab3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(310, 450, 181, 31))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(16, 16))
        self.pushButton_12 = QPushButton(self.tab3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(120, 450, 181, 31))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QSize(16, 16))
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043b\u0438\u0446\u0430", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u044b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.comboBox.setCurrentText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043e\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0434\u043e", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0448\u0438\u043d\u044b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID \u0432\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u0430", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID \u043c\u0430\u0448\u0438\u043d\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043c\u0438\u0442 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0430", None))
    # retranslateUi

