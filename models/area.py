"""Area Class Module"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey, String


class Area(BaseModel):
    """Area Class Model"""
    __tablename__ = 'areas'
    name = mapped_column(String(16), nullable=False)
    cities = relationship('City', backref='area')
    region_id = mapped_column(ForeignKey('regions.id'))

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
