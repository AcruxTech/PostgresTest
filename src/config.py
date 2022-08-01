import os
import dotenv

dotenv.load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS') 
DB_NAME = os.getenv('DB_NAME') 