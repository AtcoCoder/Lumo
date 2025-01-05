from models.base_model import BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, ForeignKey


class City(BaseModel):
    """City class"""
    __tablename__ = 'cities'
    name = mapped_column(String(60), nullable=False)
    area_id = mapped_column(ForeignKey('areas.id'))
    properties = relationship('Property', back_populates='city')

    def __init__(self, **kwargs) -> None:
        """Initialises city instance"""
        super().__init__(**kwargs)
    
    def return_location(self):
        """Return full location of city"""
        city_name = self.name
        area_name = self.area.name
        region_name = self.area.region.name
        location = [city_name, area_name, region_name]
        return ', '.join(location)
