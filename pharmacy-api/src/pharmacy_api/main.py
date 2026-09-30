from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.repositories.user.migrations import Migrate
from pharmacy_api.repositories.user.user import UserRepository



def main():
    connection = database.DBConnection()
    Migrate(connection=connection)
    user_repo = UserRepository(connection=connection)
    if user_repo!= None:
        print("UserRepository initialized successfully.")


if __name__ == "__main__":
    main()
