#queries

#tables
from pharmacy_api.router.routes import create_medications_blueprint


CreateEmployeeTable="""CREATE TABLE IF NOT EXISTS Employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""


CreateCategoriesTable = """
CREATE TABLE IF NOT EXISTS Categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT
);
"""

CreateMedicationsTable = """
CREATE TABLE IF NOT EXISTS Medications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    expiration_date DATE NOT NULL
);
"""

#Employee

CheckExistsEmployeesQuery="SELECT * FROM Employees WHERE username = %s"

GetEmployeesQuery="SELECT * FROM Employees"

AddUserQuery="INSERT INTO Employees (id, name, lastname, dni, email, position, username, password) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)"

UpdateUserQuery="UPDATE Employees SET name = %s, lastname = %s, dni = %s, email = %s, position = %s WHERE username = %s"

DeleteUserQuery="DELETE FROM Employees WHERE username = %s"

ChangePwdQuery="UPDATE Employees SET password = %s WHERE username = %s"


#Categories


CheckExistsCategoriesQuery = "SELECT 1 FROM Categories WHERE code = %s LIMIT 1;"

GetCategoriesQuery = "SELECT * FROM Categories;"

GetCategoryByCodeQuery = "SELECT * FROM Categories WHERE code = %s;"

AddCategoryQuery = "INSERT INTO Categories (code, name, description) VALUES (%s, %s, %s);"

UpdateCategoryQuery = "UPDATE Categories SET name = %s, description = %s WHERE code = %s;"

DeleteCategoryQuery = "DELETE FROM Categories WHERE code = %s;"

#Medications

CheckExistsMedicationsQuery="SELECT * FROM Medications WHERE name = %s"

GetAllMedicationsQuery="SELECT * FROM Medications"

AddMedicationQuery="INSERT INTO Medications (id, name, price, stock, category, expiration_date) VALUES (DEFAULT, %s, %s, %s, %s, %s)"

UpdateMedicationQuery="UPDATE Medications SET name = %s, price = %s, stock = %s, category = %s, expiration_date = %s WHERE name = %s"

DeleteMedicationQuery="DELETE FROM Medications WHERE name = %s"

FindMedicationByNameQuery="SELECT * FROM Medications WHERE name = %s"
