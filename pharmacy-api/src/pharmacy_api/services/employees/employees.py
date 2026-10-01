class EmployeeService:
    def __init__(self, repository):
        self.repository = repository

    def list_employees(self):
        return self.repository.ListEmployees()

    def create_user(self, user):
        self.validate_user_data(user)
        encrypted_password = self.encrypt_password(user['password'])
        user['password'] = encrypted_password
        return self.repository.NewUser(user)

    def update_user(self, user):
        self.validate_user_data(user)
        encrypted_password = self.encrypt_password(user['password'])
        user['password'] = encrypted_password
        return self.repository.EditUser(user)

    def delete_user(self, username):
        return self.repository.DeleteUser(username)

    def change_password(self, username, new_password):
        encrypted_password = self.encrypt_password(new_password)
        return self.repository.ChangePassword(username, encrypted_password)

    def find_employee_by_username(self, username):
        return self.repository.FindEmployeeByUsername(username)

    def validate_user_data(self, user):
        if not user.get('name'):
            raise ValueError("Nombre obligatorio.")
        if not user.get('last_name'):
            raise ValueError("Apellido obligatorio.")
        if not user.get('dni'):
            raise ValueError("DNI obligatorio.")
        if not self.is_valid_email(user.get('email')):
            raise ValueError("Email válido.")
        if not user.get('position'):
            raise ValueError("Cargo obligatorio.")

    def is_valid_email(self, email):
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def encrypt_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
