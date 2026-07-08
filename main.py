import sys
from PySide6.QtWidgets import QApplication


from app.app import AppLogic
"""Вся логика приложения написана в /app/app.py----"""
"""Вся логика приложения написана в /app/app.py"""
"""BUGFIX2"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppLogic()
    window.show()
    sys.exit(app.exec())