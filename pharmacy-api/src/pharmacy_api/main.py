from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.repositories.employees.migrations import Migrate
from pharmacy_api.repositories.employees.employee import EmployeeRepository



def main():
    connection = database.DBConnection()
    Migrate(connection=connection)
    employee_repo = EmployeeRepository(connection=connection)
    if employee_repo!= None:
        print("EmployeeRepo initialized successfully.")


if __name__ == "__main__":
    main()
