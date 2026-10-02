class CategoriesService:
    def __init__(self, categories_repository):
        self.categories_repository = categories_repository

    def list_categories(self):
        return self.categories_repository.list_categories()

    def new_category(self, category: dict):
        self.validate_category_data(category)
        return self.categories_repository.new_category(category)

    def edit_category(self, category: dict):
        self.validate_category_data(category)
        return self.categories_repository.edit_category(category)

    def delete_category(self, code: str):
        if not code or not code.strip():
            raise ValueError("El código de la categoría es obligatorio.")
        return self.categories_repository.delete_category(code.strip())

    def find_category_by_code(self, code: str):
        if not code or not code.strip():
            raise ValueError("El código de la categoría es obligatorio.")
        return self.categories_repository.find_category_by_code(code.strip())

    def validate_category_data(self, category: dict):
        if not category.get("code") or not str(category["code"]).strip():
            raise ValueError("El código de la categoría es obligatorio.")
        if not category.get("name") or not str(category["name"]).strip():
            raise ValueError("El nombre de la categoría es obligatorio.")
