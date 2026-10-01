from pharmacy_api.config.queries import (
    AddCategoryQuery,
    CheckExistsCategoriesQuery,
    DeleteCategoryQuery,
    UpdateCategoryQuery,
    GetCategoriesQuery,
)


class CategoriesRepository:
    def __init__(self, connection):
        self.connection = connection

    def check_exists(self, code):
        cursor = self.connection.cursor()
        cursor.execute(CheckExistsCategoriesQuery, (code,))
        return cursor.fetchone() is not None

    def ListCategories(self):
        cursor = self.connection.cursor()
        cursor.execute(GetCategoriesQuery)
        return cursor.fetchall()

    def NewCategory(self, category):
        if self.check_exists(category.code):
            return False
        cursor = self.connection.cursor()
        cursor.execute(
            AddCategoryQuery,
            (category.name, category.code, category.description),
        )
        self.connection.commit()
        return True

    def EditCategory(self, category):
        if not self.check_exists(category.code):
            return False
        cursor = self.connection.cursor()
        cursor.execute(
            UpdateCategoryQuery,
            (category.name, category.description, category.code),
        )
        self.connection.commit()
        return True

    def DeleteCategory(self, code):
        if not self.check_exists(code):
            return False
        cursor = self.connection.cursor()
        cursor.execute(DeleteCategoryQuery, (code,))
        self.connection.commit()
        return True

    def FindCategoryByCode(self, code):
        cursor = self.connection.cursor()
        cursor.execute(CheckExistsCategoriesQuery, (code,))
        return cursor.fetchone()
