"""models init module"""
from models.engine.db import DB

db = DB()
print("Reloading the database...")
db.reload()
