from sqlalchemy import (
    String,
    ForeignKey,
    Table,
    Column
)
from sqlalchemy.orm import mapped_column, relationship

from models.base_model import BaseModel, property_amenity


class Amenity(BaseModel):
    """Amenity class"""
    __tablename__ = 'amenities'
    name = mapped_column(String(16), nullable=False, unique=True)
    properties =relationship(
        'Property', secondary=property_amenity, back_populates='amenities'
    )

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
