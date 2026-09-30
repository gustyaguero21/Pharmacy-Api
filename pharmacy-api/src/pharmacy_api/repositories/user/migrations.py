def Migrate(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            ID INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            lastname VARCHAR(100),
            dni VARCHAR(20),
            phone VARCHAR(20),
            email VARCHAR(100),
            address VARCHAR(255),
            social_security VARCHAR(50),
            username VARCHAR(50),
            password VARCHAR(255)
        )
    """)

    connection.commit()