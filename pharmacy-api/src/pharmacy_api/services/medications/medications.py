class MedicationsService:
    def __init__(self, repository: MedicationsRepository):
        self.repository = repository

    def add_medication(self, medication):
        return self.repository.add_medication(medication)

    def delete_medication(self, name):
        return self.repository.delete_medication(name)

    def update_medication(self, medication):
        return self.repository.update_medication(medication)

    def get_all_medications(self):
        return self.repository.get_all_medications()

    def find_medication_by_name(self, name):
        return self.repository.find_medication_by_name(name)
