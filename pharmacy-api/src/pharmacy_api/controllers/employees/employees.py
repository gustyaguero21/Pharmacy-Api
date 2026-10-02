class EmployeeController:
    def __init__(self, employee_service):
        self.employee_service = employee_service

    def list_employees(self):
        return self.employee_service.list_employees()

    def create_user(self, user: dict):
        return self.employee_service.create_user(user)

    def update_user(self, user: dict):
        return self.employee_service.update_user(user)

    def delete_user(self, username: str):
        return self.employee_service.delete_user(username)

    def change_password(self, username: str, new_password: str):
        return self.employee_service.change_password(username, new_password)

    def find_employee_by_username(self, username: str):
        return self.employee_service.find_employee_by_username(username)
