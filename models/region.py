"""Region Class Module"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship


class Region(BaseModel):
    """Region Class Model"""
    __tablename__ = 'regions'
    name = mapped_column(String(60), nullable=False, unique=True)
    areas = relationship('Area', backref='region')

    def __init__(self, **kwargs) -> None:
        """Initialises region instance"""
        super().__init__(**kwargs)
    
    def get_dict(self):
        """"""
        pass
