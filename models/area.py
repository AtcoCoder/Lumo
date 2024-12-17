"""Area Class Module"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class Area(BaseModel):
    """Area Class Model"""
    __tablename__ = 'areas'
    cities = relationship('City', back_populates='area')
    region_id = mapped_column(ForeignKey('regions.id'))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
