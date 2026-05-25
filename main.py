from app.database.requests import selectCars
from app.database.models import async_main

import asyncio

if __name__=="__main__":
    asyncio.run(async_main())
    print('done')