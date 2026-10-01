from pharmacy_api.config.queries import CreateCategoriesTable
from pharmacy_api.config.queries import CreateEmployeeTable

migrations = [
    (CreateCategoriesTable, "CreateCategoriesTable"),
    (CreateEmployeeTable, "CreateEmployeeTable")
]

def Migrate(connection):
    cursor = connection.cursor()
    for migration, name in migrations:
        cursor.execute(migration)
        print(f"Executed migration: {name}")
    connection.commit()
