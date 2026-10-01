from pharmacy_api.config.queries import (
    AddMedicationQuery,
    DeleteMedicationQuery,
    UpdateMedicationQuery,
    GetAllMedicationsQuery,
    CheckExistsMedicationsQuery,
    FindMedicationByNameQuery,
)

class MedicationsRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_medication(self, medication):
        cursor = self.connection.cursor()
        cursor.execute(
            AddMedicationQuery,
            (medication.name, medication.price, medication.stock, medication.category, medication.expiration_date),
        )
        self.connection.commit()
        return True

    def delete_medication(self, name):
        cursor = self.connection.cursor()
        cursor.execute(DeleteMedicationQuery, (name,))
        self.connection.commit()
        return True

    def update_medication(self, medication):
        cursor = self.connection.cursor()
        cursor.execute(
            UpdateMedicationQuery,
            (medication.name, medication.price, medication.stock, medication.category, medication.expiration_date, medication.name),
        )
        self.connection.commit()
        return True

    def get_all_medications(self):
        cursor = self.connection.cursor()
        cursor.execute(GetAllMedicationsQuery)
        return cursor.fetchall()

    def find_medication_by_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute(FindMedicationByNameQuery, (name,))
        return cursor.fetchone()
