from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.config.migrations import Migrate
from pharmacy_api.models.medications.medications import Medications
from pharmacy_api.repositories.employees.employee import EmployeesRepository
from pharmacy_api.repositories.categories.categories import CategoriesRepository
from pharmacy_api.repositories.medications.medications import MedicationsRepository



def main():
    connection = database.DBConnection()
    Migrate(connection=connection)
    EmployeesRepository(connection=connection)
    CategoriesRepository(connection=connection)
    MedicationsRepository(connection=connection)



if __name__ == "__main__":
    main()
