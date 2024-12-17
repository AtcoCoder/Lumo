"""Property class module"""
import enum
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy import Enum, Boolean
from models.base_model import BaseModel
from models.amenity import property_amenity
from sqlalchemy.orm import relationship

NOT_NULLABLES = [
    'title',
    'user_id',
    'price',
    'location',
    'size'
]


class Property(BaseModel):
    """Property class"""
    __tablename__ = 'properties'
    title = mapped_column(String(255), nullable=False)
    user_id = mapped_column(ForeignKey('users.id'))
    price = mapped_column(Integer, nullable=False)
    location = mapped_column(String(255), nullable=False)
    description = mapped_column(Text, nullable=True)
    property_type = mapped_column(Enum('rent', 'sale'), nullable=False)
    is_active = mapped_column(Boolean, nullable=True)
    city_id = mapped_column(ForeignKey('cities.id'))
    amenities = relationship(
        'Amenity', secondary=property_amenity, back_populates='properties'
    )

    def __init__(self, **kwargs) -> None:
        for not_null in NOT_NULLABLES:
            if not_null not in kwargs:
                raise AttributeError(f'Property must be created with a {not_null}')
        super().__init__(**kwargs)
