from app.database.models import async_assign
from app.database.models import Car, Prava, Owner

from sqlalchemy import select, update,delete,desc

# async def set_user(tg_id,username,name,email,phone):
#     async with async_assign() as session:
#         user=  await session.scalar(select(User).where(User.tg_id==tg_id))

#         if not user:
#            session.add(User(tg_id=tg_id,name=name,username=username,email=email,phone=phone))    
#            await session.commit()       





# async def update_user(tg_id, username: str = None, name: str = None, 
#                      email: str = None, phone: str = None):
#     async with async_assign() as session:
#         user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
#         if not user:
#             await set_user(tg_id=tg_id,username=username,name=name,phone=phone,email=email)
#             await session.commit()
        
#         else:

#             user.username = username

#             user.name = name

#             user.email = email
    
#             user.phone = phone
            
#             await session.commit()
#         return user


async def selectCars():
    async with async_assign() as session:
        return await session.scalar(select(Car))
    
    

# async def get_maincategories():
#     async with async_assign() as session:
#         return await session.scalars(select(Main_Category))



# async def get_categories(main_category_id):
#     async with async_assign() as session:
#         return await session.scalars(select(Category).where(Category.main_category== main_category_id))
    
# async def get_items(category_id):
#     async with async_assign() as session:
#         return await session.scalars(select(Item).where(Item.category==category_id))

# async def get_item(item_id):
#     async with async_assign() as session:
#         return await session.scalars(select(Item).where(Item.id==item_id))    

