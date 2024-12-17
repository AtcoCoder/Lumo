"""Image class Module"""
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column


class Image(BaseModel):
    """Image class model"""
    __tablename__ = 'images'
    image_url = mapped_column(String(255), nullable=False)
    property_id = mapped_column(ForeignKey('properties.id'))

    def __init__(self, **kwargs) -> None:
        """Initialises image instance"""
        super().__init__(**kwargs)
    
    @property
    def uploaded_at(self):
        """Returns created_at of image"""
        return self.created_at
