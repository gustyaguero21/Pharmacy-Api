class EmployeeController:
    def __init__(self, service):
        self.service = service

    def list_employees(self):
        return self.service.list_employees()

    def create_user(self, user):
        return self.service.create_user(user)

    def update_user(self, user):
        return self.service.update_user(user)

    def delete_user(self, username):
        return self.service.delete_user(username)

    def change_password(self, username, new_password):
        return self.service.change_password(username, new_password)

    def find_employee_by_username(self, username):
        return self.service.find_employee_by_username(username)
