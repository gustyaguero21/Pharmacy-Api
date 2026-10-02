class MedicationsService:
    def __init__(self, medications_repository):
        self.medications_repository = medications_repository

    def get_all_medications(self):
        return self.medications_repository.get_all_medications()

    def add_medication(self, medication_data: dict):
        validated_data = self.validate_and_clean_medication_data(medication_data)
        return self.medications_repository.add_medication(validated_data)

    def update_medication(self, medication_data: dict):
        validated_data = self.validate_and_clean_medication_data(medication_data)
        return self.medications_repository.update_medication(validated_data)

    def delete_medication(self, name: str):
        if not name or not name.strip():
            raise ValueError("El nombre del medicamento es obligatorio.")
        return self.medications_repository.delete_medication(name.strip())

    def find_medication_by_name(self, name: str):
        if not name or not name.strip():
            raise ValueError("El nombre del medicamento es obligatorio.")
        return self.medications_repository.find_medication_by_name(name.strip())

    def validate_and_clean_medication_data(self, data: dict) -> dict:
        name = str(data.get("name", "")).strip()
        if not name:
            raise ValueError("El nombre del medicamento es obligatorio.")

        try:
            price = float(data.get("price", 0))
            if price <= 0:
                raise ValueError("El precio debe ser un número positivo mayor a 0.")
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un valor numérico válido.")

        try:
            stock = int(data.get("stock", 0))
            if stock < 0:
                raise ValueError("El stock no puede ser negativo.")
        except (ValueError, TypeError):
            raise ValueError("El stock debe ser un número entero válido.")

        category = str(data.get("category", "")).strip()
        if not category:
            raise ValueError("La categoría es obligatoria.")

        expiration_date = str(data.get("expiration_date", "")).strip()
        if not expiration_date:
            raise ValueError("La fecha de vencimiento es obligatoria.")

        return {
            "name": name,
            "price": price,
            "stock": stock,
            "category": category,
            "expiration_date": expiration_date,
        }
