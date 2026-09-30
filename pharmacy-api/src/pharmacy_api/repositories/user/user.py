class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, username):
        cursor = self.connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone() is not None

    def NewUser(self, user):
        if self.check_exists(user.username):
            return False
        cursor = self.connection.cursor()
        query = "INSERT INTO users (id, name, lastname, dni, phone, email, address, social_security, username, password) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (user.name, user.lastname, user.dni, user.phone, user.email, user.address, user.social_security, user.username, user.password))
        self.connection.commit()
        return True

    def EditUser(self, user):
        if not self.check_exists(user.username):
            return False
        cursor = self.connection.cursor()
        query = "UPDATE users SET name = %s, lastname = %s, dni = %s, phone = %s, email = %s, address = %s, social_security = %s WHERE username = %s"
        cursor.execute(query, (user.name, user.lastname, user.dni, user.phone, user.email, user.address, user.social_security, user.username))
        self.connection.commit()
        return True

    def DeleteUser(self, username):
        if not self.check_exists(username):
            return False
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        self.connection.commit()
        return True

    def ChangePassword(self, username, new_password):
        if not self.check_exists(username):
            return False
        cursor = self.connection.cursor()
        query = "UPDATE users SET password = %s WHERE username = %s"
        cursor.execute(query, (new_password, username))
        self.connection.commit()
        return True