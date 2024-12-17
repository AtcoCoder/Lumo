"""Property class module"""
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey
from models.base_model import BaseModel
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

    def __init__(self, **kwargs) -> None:
        for not_null in NOT_NULLABLES:
            if not_null not in kwargs:
                raise AttributeError(f'Property must be created with a {not_null}')
        super().__init__(**kwargs)
