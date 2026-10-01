from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.config.migrations import Migrate
from pharmacy_api.repositories.employees.employee import EmployeeRepository
from pharmacy_api.repositories.categories.categories import CategoriesRepository



def main():
    connection = database.DBConnection()
    Migrate(connection=connection)
    EmployeeRepository(connection=connection)
    CategoriesRepository(connection=connection)


if __name__ == "__main__":
    main()
