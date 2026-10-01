from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.config.migrations import Migrate
from pharmacy_api.models.medications.medications import Medications
from pharmacy_api.repositories.employees.employee import EmployeesRepository
from pharmacy_api.repositories.categories.categories import CategoriesRepository
from pharmacy_api.repositories.medications.medications import MedicationsRepository
from pharmacy_api.services.employees.employees import EmployeeService
from pharmacy_api.services.categories.categories import CategoriesServices
from pharmacy_api.services.medications.medications import MedicationsService



def main():
    #levanta la base de datos mysql.
    connection = database.DBConnection()
    #crea las tablas en una migracion controlada mediante la funcion Migrate.
    Migrate(connection=connection)
    #inicializa los repositorios para interactuar con la base de datos.
    employee_repository = EmployeesRepository(connection=connection)
    categories_repository = CategoriesRepository(connection=connection)
    medications_repository = MedicationsRepository(connection=connection)
    #inicializa los servicios para interactuar con los repositorios.
    employee_service = EmployeeService(repository=employee_repository)
    categories_service = CategoriesServices(repository=categories_repository)
    medications_service = MedicationsService(repository=medications_repository)




if __name__ == "__main__":
    main()
