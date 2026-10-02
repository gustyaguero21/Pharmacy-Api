from pharmacy_api.config.queries import (
    AddCategoryQuery,
    CheckExistsCategoriesQuery,
    DeleteCategoryQuery,
    GetCategoriesQuery,
    GetCategoryByCodeQuery,  # Se recomienda tener una consulta específica para traer el registro
    UpdateCategoryQuery,
)


class CategoriesRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, code: str) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(CheckExistsCategoriesQuery, (code,))
            return cursor.fetchone() is not None

    def list_categories(self):
        with self.connection.cursor() as cursor:
            cursor.execute(GetCategoriesQuery)
            return cursor.fetchall()

    def new_category(self, category: dict) -> bool:
        if self.check_exists(category["code"]):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(
                AddCategoryQuery,
                (category["name"], category["code"], category.get("description", "")),
            )
        self.connection.commit()
        return True

    def edit_category(self, category: dict) -> bool:
        if not self.check_exists(category["code"]):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(
                UpdateCategoryQuery,
                (category["name"], category.get("description", ""), category["code"]),
            )
        self.connection.commit()
        return True

    def delete_category(self, code: str) -> bool:
        if not self.check_exists(code):
            return False

        with self.connection.cursor() as cursor:
            cursor.execute(DeleteCategoryQuery, (code,))
        self.connection.commit()
        return True

    def find_category_by_code(self, code: str):
        with self.connection.cursor() as cursor:
            cursor.execute(GetCategoryByCodeQuery, (code,))
            return cursor.fetchone()
