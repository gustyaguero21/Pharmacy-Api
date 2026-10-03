from pharmacy_api.database import database
from pharmacy_api.config import env
from pharmacy_api.config.migrations import Migrate
from pharmacy_api.models.medications.medications import Medications
from pharmacy_api.repositories.employees.employee import EmployeesRepository
from pharmacy_api.repositories.categories.categories import CategoriesRepository
from pharmacy_api.repositories.medications.medications import MedicationsRepository
from pharmacy_api.router.server import create_app
from pharmacy_api.services.employees.employees import EmployeeService
from pharmacy_api.services.categories.categories import CategoriesService
from pharmacy_api.services.medications.medications import MedicationsService
from pharmacy_api.controllers.employees.employees import EmployeeController
from pharmacy_api.controllers.categories.categories import CategoriesController
from pharmacy_api.controllers.medications.medications import MedicationsController


def main():
    # Levanta la base de datos mysql y corre migraciones iniciales
    connection = database.DBConnection()
    Migrate(connection=connection)

    # Inicializa los repositorios
    # NOTA: Para evitar el error (0, '') asegúrate que tus repositorios
    # abran/cierren una conexión o usen un pool por cada consulta HTTP.
    employee_repository = EmployeesRepository(connection=connection)
    categories_repository = CategoriesRepository(connection=connection)
    medications_repository = MedicationsRepository(connection=connection)

    # Inicializa los servicios
    employee_service = EmployeeService(employee_repository=employee_repository)
    categories_service = CategoriesService(categories_repository=categories_repository)
    medications_service = MedicationsService(medications_repository=medications_repository)

    # Inicializa los controladores
    employee_controller = EmployeeController(employee_service=employee_service)
    categories_controller = CategoriesController(categories_service=categories_service)
    medications_controller = MedicationsController(medications_service=medications_service)

    # Crea la aplicación Flask
    app = create_app(employee_controller, categories_controller, medications_controller)

    return app


if __name__ == "__main__":
    app = main()
    app.run(debug=True, port=5000)
