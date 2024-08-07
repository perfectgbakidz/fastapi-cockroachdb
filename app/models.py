from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ARRAY
from .database import Base

class Apartment(Base):
    __tablename__ = "apartments"

    apartment_id = Column(Integer, primary_key=True, index=True)
    area = Column(String, nullable=False)
    water_source = Column(String(50))
    electricity_meter = Column(String(50))
    apartment_type = Column(String(50))
    private_toilet = Column(Boolean)
    rent_per_month = Column(DECIMAL(10, 2), nullable=False)
    yearly_payment = Column(DECIMAL(10, 2), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    agent_fee = Column(DECIMAL(10, 2), nullable=False)
    inspection_fee = Column(DECIMAL(10, 2), nullable=False)
    electricity_included = Column(Boolean)
    pictures = Column(ARRAY(String))
    videos = Column(ARRAY(String))
