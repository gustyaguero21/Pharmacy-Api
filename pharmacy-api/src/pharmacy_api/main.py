from pharmacy_api.database import database
from pharmacy_api.config import env



def main():
    database.DBConnection()


if __name__ == "__main__":
    main()
