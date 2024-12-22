from sqlalchemy import (
    String,
    ForeignKey,
    Table,
    Column,
    Integer
)
from sqlalchemy.orm import mapped_column, relationship
from models.base_model import Base, BaseModel


property_amenity = Table(
    'property_amenity', Base.metadata,
    Column('property_id', String(60), ForeignKey('properties.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)


class Amenity(BaseModel):
    """Amenity class"""
    __tablename__ = 'amenities'
    name = mapped_column(String(32), nullable=False, unique=True)
    amount = mapped_column(Integer, nullable=False)
    properties =relationship(
        'Property', secondary=property_amenity, back_populates='amenities'
    )

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
