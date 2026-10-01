class MedicationsController:
    def __init__(self, service: MedicationsService):
        self.service = service

    def add_medication(self, request):
        medication = Medications(
            name=request.form['name'],
            price=float(request.form['price']),
            stock=int(request.form['stock']),
            category=request.form['category'],
            expiration_date=request.form['expiration_date']
        )
        return self.service.add_medication(medication)

    def delete_medication(self, request):
        return self.service.delete_medication(request.form['name'])

    def update_medication(self, request):
        medication = Medications(
            name=request.form['name'],
            price=float(request.form['price']),
            stock=int(request.form['stock']),
            category=request.form['category'],
            expiration_date=request.form['expiration_date']
        )
        return self.service.update_medication(medication)

    def get_all_medications(self, request):
        return self.service.get_all_medications()

    def find_medication_by_name(self, request):
        return self.service.find_medication_by_name(request.form['name'])
