from models.base_model import BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, ForeignKey


class City(BaseModel):
    """City class"""
    __tablename__ = 'cities'
    name = mapped_column(String(60), nullable=False, unique=True)
    area_id = mapped_column(ForeignKey('areas.id'))
    properties = relationship('Property', back_populates='city')

    def __init__(self, **kwargs) -> None:
        """Initialises city instance"""
        super().__init__(**kwargs)
