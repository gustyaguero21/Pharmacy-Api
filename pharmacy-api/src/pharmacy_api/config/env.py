from dotenv import load_dotenv
import os

def get_db_host():
    load_dotenv()
    return os.getenv('DB_HOST')

def get_db_port():
    load_dotenv()
    return os.getenv('DB_PORT')

def get_db_user():
    load_dotenv()
    return os.getenv('DB_USER')

def get_db_password():
    load_dotenv()
    return os.getenv('DB_PASSWORD')

def get_db_name():
    load_dotenv()
    return os.getenv('DB_NAME')
