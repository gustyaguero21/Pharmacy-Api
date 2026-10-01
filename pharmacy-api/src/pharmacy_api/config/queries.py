#queries

#tables
CreateEmployeeTable="""CREATE TABLE IF NOT EXISTS Employees (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""

CreateCategoriesTable="""CREATE TABLE IF NOT EXISTS Categories (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255)
)
"""


#Employee

CheckExistsEmployeesQuery="SELECT * FROM Employees WHERE username = %s"

GetEmployeesQuery="SELECT * FROM Employees"

AddUserQuery="INSERT INTO Employees (id, name, lastname, dni, email, position, username, password) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)"

UpdateUserQuery="UPDATE Employees SET name = %s, lastname = %s, dni = %s, email = %s, position = %s WHERE username = %s"

DeleteUserQuery="DELETE FROM Employees WHERE username = %s"

ChangePwdQuery="UPDATE Employees SET password = %s WHERE username = %s"


#Categories

CheckExistsCategoriesQuery="SELECT * FROM Categories WHERE code = %s"

GetCategoriesQuery="SELECT * FROM Categories"

AddCategoryQuery="INSERT INTO Categories (id, name, code, description) VALUES (DEFAULT, %s, %s, %s)"

UpdateCategoryQuery="UPDATE Categories SET name = %s, code = %s, description = %s WHERE id = %s"

DeleteCategoryQuery="DELETE FROM Categories WHERE id = %s"
