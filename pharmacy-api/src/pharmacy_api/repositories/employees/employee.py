from pharmacy_api.config.queries import (
    AddUserQuery,
    ChangePwdQuery,
    CheckExistsEmployeesQuery,
    DeleteUserQuery,
    UpdateUserQuery,
    GetEmployeesQuery,
)


class EmployeeRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, username):
        cursor = self.connection.cursor()
        cursor.execute(CheckExistsEmployeesQuery, (username,))
        return cursor.fetchone() is not None

    def ListEmployees(self):
        cursor = self.connection.cursor()
        cursor.execute(GetEmployeesQuery)
        return cursor.fetchall()

    def NewUser(self, user):
        if self.check_exists(user.username):
            return False
        cursor = self.connection.cursor()
        cursor.execute(
            AddUserQuery,
            (user.name, user.lastname, user.dni, user.email, user.position, user.username, user.password),
        )
        self.connection.commit()
        return True

    def EditUser(self, user):
        if not self.check_exists(user.username):
            return False
        cursor = self.connection.cursor()
        cursor.execute(
            UpdateUserQuery,
            (user.name, user.lastname, user.dni, user.email, user.position, user.username),
        )
        self.connection.commit()
        return True

    def DeleteUser(self, username):
        if not self.check_exists(username):
            return False
        cursor = self.connection.cursor()
        cursor.execute(DeleteUserQuery, (username,))
        self.connection.commit()
        return True

    def ChangePassword(self, username, new_password):
        if not self.check_exists(username):
            return False
        cursor = self.connection.cursor()
        cursor.execute(ChangePwdQuery, (new_password, username))
        self.connection.commit()
        return True

    def FindEmployeeByUsername(self, username):
        cursor = self.connection.cursor()
        cursor.execute(CheckExistsEmployeesQuery, (username,))
        return cursor.fetchone()
