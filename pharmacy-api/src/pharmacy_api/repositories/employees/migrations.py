from pharmacy_api.config.queries import CreateEmployeeTable


def Migrate(connection):
    cursor = connection.cursor()
    cursor.execute(CreateEmployeeTable)

    connection.commit()
