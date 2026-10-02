from pharmacy_api.config.queries import (
    CheckExistsCategoriesQuery,
    GetCategoriesQuery,
    AddCategoryQuery,
    UpdateCategoryQuery,
    DeleteCategoryQuery,
    GetCategoryByCodeQuery
)


class CategoriesRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, code: str) -> bool:
        cursor = self.connection.cursor()
        try:
            # Normalizamos a mayúsculas y quitamos espacios
            clean_code = str(code).strip().upper()
            cursor.execute(CheckExistsCategoriesQuery, (clean_code,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()

    def list_categories(self):
        with self.connection.cursor() as cursor:
            cursor.execute(GetCategoriesQuery)
            return cursor.fetchall()

    def new_category(self, category: dict) -> bool:
        if self.check_exists(category["code"]):
            return False

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                AddCategoryQuery,
                (
                    category["code"],  # 1º Posición: code (Primary Key)
                    category["name"],  # 2º Posición: name
                    category.get("description", ""),  # 3º Posición: description
                ),
            )
            self.connection.commit()
            return True
        finally:
            cursor.close()

    def edit_category(self, category: dict) -> bool:
        if not self.check_exists(category["code"]):
            return False

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                UpdateCategoryQuery,
                (
                    category["name"],
                    category.get("description", ""),
                    category["code"],
                ),
            )
            self.connection.commit()
            # Retorna True si modificó al menos una fila
            return cursor.rowcount > 0
        finally:
            cursor.close()

    def delete_category(self, code: str) -> bool:
        if not self.check_exists(code):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(DeleteCategoryQuery, (code,))
        self.connection.commit()
        return True

    def find_category_by_code(self, code: str):
            cursor = self.connection.cursor()
            cursor.execute(GetCategoryByCodeQuery, (code,))
            row = cursor.fetchone()

            if not row:
                cursor.close()
                return None
            columns = [column[0] for column in cursor.description]
            category = dict(zip(columns, row))

            cursor.close()
            return category
