from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/apartments/", response_model=schemas.Apartment)
async def create_apartment(apartment: schemas.ApartmentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_apartment(db=db, apartment=apartment)

@app.get("/apartments/", response_model=List[schemas.Apartment])
async def read_apartments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_apartments(db=db, skip=skip, limit=limit)
