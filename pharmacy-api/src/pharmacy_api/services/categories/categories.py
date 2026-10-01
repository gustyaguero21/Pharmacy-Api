class CategoriesServices:
    def __init__(self, categories_repository):
        self.categories_repository = categories_repository

    def list_categories(self):
        return self.categories_repository.ListCategories()

    def new_category(self, category):
        return self.categories_repository.NewCategory(category)

    def edit_category(self, category):
        return self.categories_repository.EditCategory(category)

    def delete_category(self, code):
        return self.categories_repository.DeleteCategory(code)

    def find_category_by_code(self, code):
        return self.categories_repository.FindCategoryByCode(code)
