from models.engine.db import DB
from config import Development

db = DB(Development.DATABASE_URI)
db.reload()
