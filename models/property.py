"""Property class module"""
import enum
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey, Text, text, Index
from sqlalchemy import Enum, Boolean
from models.base_model import BaseModel
from models.amenity import property_amenity
from sqlalchemy.orm import relationship

NOT_NULLABLES = [
    'title',
    'user_id',
    'price',
    'location'
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
    city = relationship('City', back_populates='properties')
    amenities = relationship(
        'Amenity', secondary=property_amenity, back_populates='properties'
    )
    images = relationship('Image', backref='property')

    __table_args__ = (
        Index('idx_fulltext_title_description', 'title', 'description', mysql_prefix='FULLTEXT'),
    )

    def __init__(self, **kwargs) -> None:
        for not_null in NOT_NULLABLES:
            if not_null not in kwargs:
                raise AttributeError(f'Property must be created with a {not_null}')
        super().__init__(**kwargs)

    @classmethod
    def search(cls, search_query):
        """search for properties in the search_query"""
        from models import db
        # search_terms = search_query.split()

        # query = db.session.query(cls)
        # for term in search_terms:
        #     query = query.filter(cls.title.like(f"%{term}%"))
        # results = query.all(
        results = db.session.query(cls).from_statement(
            text("""\
            SELECT *, MATCH(title, description) AGAINST(:query) AS relevance \
            FROM properties \
            WHERE MATCH(title, description) AGAINST(:query) \
            ORDER BY relevance DESC\
            """)
        ).params(query=search_query).all()
        print(results)
        return results