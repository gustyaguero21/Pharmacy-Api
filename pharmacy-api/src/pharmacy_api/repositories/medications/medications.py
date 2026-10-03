import config.env

from pharmacy_api.config.queries import (
    AddMedicationQuery,
    CheckExistsMedicationsQuery,
    DeleteMedicationQuery,
    FindMedicationByNameQuery,
    GetAllMedicationsQuery,
    UpdateMedicationQuery,
)


class MedicationsRepository:
    def __init__(self, connection):
        self.connection = connection

    def _get_cursor(self):
        self.connection.ping(reconnect=True)

        db_name = config.env.get_db_name()
        self.connection.select_db(db_name)

        return self.connection.cursor()

    def check_exists(self, name: str) -> bool:
        with self._get_cursor() as cursor:
            cursor.execute(CheckExistsMedicationsQuery, (name,))
            return cursor.fetchone() is not None

    def add_medication(self, medication: dict) -> bool:
        if self.check_exists(medication["name"]):
            return False

        with self._get_cursor() as cursor:
            cursor.execute(
                AddMedicationQuery,
                (
                    medication["name"],
                    medication["price"],
                    medication["stock"],
                    medication["category"],
                    medication["expiration_date"],
                ),
            )

        self.connection.commit()
        return True

    def update_medication(self, medication: dict) -> bool:
        if not self.check_exists(medication["name"]):
            return False

        with self._get_cursor() as cursor:
            cursor.execute(
                UpdateMedicationQuery,
                (
                    medication["name"],
                    medication["price"],
                    medication["stock"],
                    medication["category"],
                    medication["expiration_date"],
                    medication["name"],
                ),
            )

        self.connection.commit()
        return True

    def delete_medication(self, name: str) -> bool:
        if not self.check_exists(name):
            return False

        with self._get_cursor() as cursor:
            cursor.execute(DeleteMedicationQuery, (name,))

        self.connection.commit()
        return True

    def get_all_medications(self):
        with self._get_cursor() as cursor:
            cursor.execute(GetAllMedicationsQuery)
            return cursor.fetchall()

    def find_medication_by_name(self, name: str):
        with self._get_cursor() as cursor:
            cursor.execute(FindMedicationByNameQuery, (name,))
            return cursor.fetchone()
