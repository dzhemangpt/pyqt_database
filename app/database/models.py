from sqlalchemy import BigInteger, String, ForeignKey, Column, LargeBinary

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column, Relationship
from sqlalchemy import Date
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine
import datetime as dt

engine = create_async_engine(url='sqlite+aiosqlite:///auto.db')

async_assign=async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Prava(Base):
    __tablename__='prava'
    
    id_prav: Mapped[int]=mapped_column(primary_key=True)
    id_car:Mapped[int]=mapped_column(ForeignKey('cars.id'))
    id_owner:Mapped[int]=mapped_column(ForeignKey('owners.id'))
    

class Owner(Base):
    __tablename__='owners'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30)) 
    surname:Mapped[str]=mapped_column(String(30)) 
    otch:Mapped[str]=mapped_column(String(30)) 
    phone:Mapped[str]=mapped_column(String(30)) 
    city:Mapped[str]=mapped_column(String(30)) 
    street:Mapped[str]=mapped_column(String(30)) 
    home:Mapped[str]=mapped_column(String(30)) 


class Car(Base):
    __tablename__='cars'
    id: Mapped[int]=mapped_column(primary_key=True)
    mark:Mapped[str]= mapped_column(String(25))
    model:Mapped[str]= mapped_column(String(25))
    color:Mapped[str]= mapped_column(String(25))
    power:Mapped[int]=mapped_column()

class Vydacha(Base):
    __tablename__='vydacha'
    id: Mapped[int]=mapped_column(primary_key=True)
    id_owner:Mapped[int]=mapped_column(ForeignKey('owners.id'))
    
    date:Mapped[dt.date] = mapped_column(Date, default=dt.date.today)
    vydal:Mapped[str]= mapped_column(String(25))
    




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

