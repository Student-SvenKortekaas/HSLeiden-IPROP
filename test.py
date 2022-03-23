from app.database import get_config, get_db


config = get_config()

cursor = get_db(**config)
print(cursor)