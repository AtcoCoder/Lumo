"""Region Class Module"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship


class Region(BaseModel):
    """Region Class Model"""
    __tablename__ = 'regions'
    name = mapped_column(String(16), nullable=False)
    areas = relationship('Area', backref='region')

    def __init__(self, **kwargs) -> None:
        """Initialises region instance"""
        super().__init__(**kwargs)
