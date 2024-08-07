from pydantic import BaseModel
from typing import List, Optional

class ApartmentCreate(BaseModel):
    area: str
    water_source: Optional[str]
    electricity_meter: Optional[str]
    apartment_type: Optional[str]
    private_toilet: Optional[bool]
    rent_per_month: float
    yearly_payment: float
    total_price: float
    agent_fee: float
    inspection_fee: float
    electricity_included: Optional[bool]
    pictures: Optional[List[str]]
    videos: Optional[List[str]]

class Apartment(ApartmentCreate):
    apartment_id: int

    class Config:
        orm_mode = True
