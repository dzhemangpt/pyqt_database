from app.database.requests import selectCars
from app.database.models import async_main

import asyncio
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    asyncio.run(async_main())
    print('done')
    # Загружаем интерфейс из файла myform.ui
    window = uic.loadUi("app/ui/main.ui")
    
    # Показываем окно
    window.show()

    sys.exit(app.exec())
