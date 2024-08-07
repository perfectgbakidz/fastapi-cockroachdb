from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_apartment(db: AsyncSession, apartment: schemas.ApartmentCreate):
    db_apartment = models.Apartment(**apartment.dict())
    db.add(db_apartment)
    await db.commit()
    await db.refresh(db_apartment)
    return db_apartment

async def get_apartments(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Apartment).offset(skip).limit(limit))
    return result.scalars().all()
