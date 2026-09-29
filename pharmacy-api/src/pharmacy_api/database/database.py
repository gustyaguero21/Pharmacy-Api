import pymysql
import config.env


def DBConnection():
    db_host = config.env.get_db_host()
    db_port = int(config.env.get_db_port())
    db_user = config.env.get_db_user()
    db_password = config.env.get_db_password()
    db_name = config.env.get_db_name()

    if not db_name.replace("_", "").isalnum():
        print(f"Database configuration error: Invalid database name {db_name!r}")
        return None

    connection = None
    try:
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
        )

        print("Connected to MySQL successfully.")

        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")

        print(f"Database '{db_name}' created or already exists.")

        connection.select_db(db_name)
        print(f"DATABASE FOUND. USING '{db_name}'...")

        return connection

    except Exception as error:
        print(f"Error handling database connection: {error}")
        if connection:
            connection.close()
        return None
