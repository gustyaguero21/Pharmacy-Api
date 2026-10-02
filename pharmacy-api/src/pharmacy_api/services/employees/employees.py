import re
import bcrypt

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

class EmployeeService:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def list_employees(self):
        return self.employee_repository.list_employees()

    def create_user(self, user: dict):
        self.validate_user_data(user)
        if not user.get("password"):
            raise ValueError("Contraseña obligatoria.")

        user["password"] = self.hash_password(user["password"])
        return self.employee_repository.new_user(user)

    def update_user(self, user: dict):
        self.validate_user_data(user)
        return self.employee_repository.edit_user(user)

    def delete_user(self, username: str):
        return self.employee_repository.delete_user(username)

    def change_password(self, username: str, new_password: str):
        if not new_password:
            raise ValueError("La nueva contraseña no puede estar vacía.")

        hashed_password = self.hash_password(new_password)
        return self.employee_repository.change_password(username, hashed_password)

    def find_employee_by_username(self, username: str):
        return self.employee_repository.find_employee_by_username(username)

    def validate_user_data(self, user: dict):
        if not user.get("name"):
            raise ValueError("Nombre obligatorio.")
        if not user.get("last_name"):
            raise ValueError("Apellido obligatorio.")
        if not user.get("dni"):
            raise ValueError("DNI obligatorio.")
        if not self.is_valid_email(user.get("email", "")):
            raise ValueError("Email no válido.")
        if not user.get("position"):
            raise ValueError("Cargo obligatorio.")
        if not user.get("username"):
            raise ValueError("Nombre de usuario obligatorio.")

    def is_valid_email(self, email: str) -> bool:
        return re.match(EMAIL_REGEX, email) is not None

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
