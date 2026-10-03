from pharmacy_api.config.queries import (
    CheckExistsCategoriesQuery,
    GetCategoriesQuery,
    AddCategoryQuery,
    UpdateCategoryQuery,
    DeleteCategoryQuery,
    GetCategoryByCodeQuery
)
# Importamos la función de conexión por si hace falta recrearla desde cero
from pharmacy_api.database.database import DBConnection


class CategoriesRepository:
    def __init__(self, connection):
        self.connection = connection

    def _ensure_connection(self):
        """Verifica que la conexión esté activa; si fue cerrada ('Already closed'), la recrea."""
        try:
            if self.connection and self.connection.open:
                self.connection.ping(reconnect=True)
            else:
                # Si la conexión se cerró por completo (self.connection.open es False), creamos una nueva
                print("Conexión de MySQL cerrada. Recreando conexión...")
                new_conn = DBConnection()
                if new_conn:
                    self.connection = new_conn
        except Exception as e:
            print(f"Error al verificar/reconectar MySQL: {e}")
            # Intentar reasignar una nueva conexión en caso de fallo
            try:
                new_conn = DBConnection()
                if new_conn:
                    self.connection = new_conn
            except Exception as rebuild_error:
                print(f"No se pudo restablecer la conexión a MySQL: {rebuild_error}")

    def check_exists(self, code: str) -> bool:
        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            clean_code = str(code).strip().upper()
            cursor.execute(CheckExistsCategoriesQuery, (clean_code,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()

    def list_categories(self):
        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            cursor.execute(GetCategoriesQuery)
            return cursor.fetchall()
        finally:
            cursor.close()

    def new_category(self, category: dict) -> bool:
        if self.check_exists(category["code"]):
            return False

        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                AddCategoryQuery,
                (
                    category["code"],
                    category["name"],
                    category.get("description", ""),
                ),
            )
            self.connection.commit()
            return True
        finally:
            cursor.close()

    def edit_category(self, category: dict) -> bool:
        if not self.check_exists(category["code"]):
            return False

        self._ensure_connection()
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
            return cursor.rowcount > 0
        finally:
            cursor.close()

    def delete_category(self, code: str) -> bool:
        if not self.check_exists(code):
            return False

        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            cursor.execute(DeleteCategoryQuery, (code,))
            self.connection.commit()
            return True
        finally:
            cursor.close()

    def find_category_by_code(self, code: str):
        self._ensure_connection()
        cursor = self.connection.cursor()
        try:
            cursor.execute(GetCategoryByCodeQuery, (code,))
            row = cursor.fetchone()

            if not row:
                return None

            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        finally:
            cursor.close()
