from sqlalchemy import BigInteger, String, ForeignKey, Column, LargeBinary

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column, Relationship

from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_assign=async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'
    
    tg_id: Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(30))
    name:Mapped[str]=mapped_column(String(25))
    phone:Mapped[str]=mapped_column(String(15))
    email:Mapped[str]=mapped_column(String(50))
    

class Main_Category(Base):
    __tablename__='maincategories'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30)) 


class Category(Base):
    __tablename__='categories'
    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]= mapped_column(String(25))
    main_category:Mapped[str]=mapped_column(String(20),ForeignKey('maincategories.id'))


class Item(Base):
    __tablename__='items'
    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]= mapped_column(String(50))
    description:Mapped[str]= mapped_column(String(300))
    price: Mapped[int]=mapped_column()
    category: Mapped[int]=mapped_column(ForeignKey('categories.id'))
    picture = Column(LargeBinary, nullable = True)
    main_category:Mapped[str]=mapped_column(String(20),ForeignKey('maincategories.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

