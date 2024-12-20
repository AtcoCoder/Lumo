from models.engine.db import DB
from config import CURRENT_CONFIG

db = DB(CURRENT_CONFIG.DATABASE_URI)
db.reload()
db.save()
