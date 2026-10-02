from pharmacy_api.config.queries import (
    AddUserQuery,
    ChangePwdQuery,
    CheckExistsEmployeesQuery,
    DeleteUserQuery,
    UpdateUserQuery,
    GetEmployeesQuery,
)


class EmployeesRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, username: str) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(CheckExistsEmployeesQuery, (username,))
            return cursor.fetchone() is not None

    def list_employees(self):
        with self.connection.cursor() as cursor:
            cursor.execute(GetEmployeesQuery)
            return cursor.fetchall()

    def new_user(self, user: dict) -> bool:
        if self.check_exists(user["username"]):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(
                AddUserQuery,
                (
                    user["name"],
                    user["last_name"],
                    user["dni"],
                    user["email"],
                    user["position"],
                    user["username"],
                    user["password"],
                ),
            )
        self.connection.commit()
        return True

    def edit_user(self, user: dict) -> bool:
        if not self.check_exists(user["username"]):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(
                UpdateUserQuery,
                (
                    user["name"],
                    user["last_name"],
                    user["dni"],
                    user["email"],
                    user["position"],
                    user["username"],
                ),
            )
        self.connection.commit()
        return True

    def delete_user(self, username: str) -> bool:
        if not self.check_exists(username):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(DeleteUserQuery, (username,))
        self.connection.commit()
        return True

    def change_password(self, username: str, new_password_hash: str) -> bool:
        if not self.check_exists(username):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(ChangePwdQuery, (new_password_hash, username))
        self.connection.commit()
        return True

    def find_employee_by_username(self, username: str):
        with self.connection.cursor() as cursor:
            cursor.execute(CheckExistsEmployeesQuery, (username,))
            return cursor.fetchone()
