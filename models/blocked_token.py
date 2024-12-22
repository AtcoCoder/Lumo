from models.base_model import BaseModel
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class BlockedToken(BaseModel):
    """Blocked Token class"""
    __tablename__ = 'blocked_tokens'
    jti = mapped_column(String(60), nullable=False)
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    @classmethod
    def get_token(cls, jti):
        """Get token from jti"""
        from models import db
        token = db.get_by(cls, 'jti', jti)
        return token

