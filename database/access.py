
from sample_config import Config
from database.database import Database

client = Database(Config.DATABASE_URL, Config.SESSION_NAME)
