class CategoriesController:
    def __init__(self, categories_service):
        self.categories_service = categories_service

    def list_categories(self):
        return self.categories_service.list_categories()

    def new_category(self, category: dict):
        return self.categories_service.new_category(category)

    def edit_category(self, category: dict):
        return self.categories_service.edit_category(category)

    def delete_category(self, code: str):
        return self.categories_service.delete_category(code)

    def find_category_by_code(self, code: str):
        return self.categories_service.find_category_by_code(code)
