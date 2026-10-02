class MedicationsController:
    def __init__(self, medications_service):
        self.service = medications_service

    def get_all_medications(self):
        return self.service.get_all_medications()

    def add_medication(self, data: dict):
        return self.service.add_medication(data)

    def update_medication(self, data: dict):
        return self.service.update_medication(data)

    def delete_medication(self, name: str):
        return self.service.delete_medication(name)

    def find_medication_by_name(self, name: str):
        return self.service.find_medication_by_name(name)
