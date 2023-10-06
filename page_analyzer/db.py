from dotenv import load_dotenv
from psycopg2 import connect
from datetime import datetime
import os


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')
