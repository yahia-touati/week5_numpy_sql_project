import os 
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_engine():
    load_dotenv()
    
    db_url = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    # Create the engine
    engine = create_engine(db_url)
    return engine
