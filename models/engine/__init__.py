"""models init module"""
from models.engine.db import DB

db = DB()
db.reload()
