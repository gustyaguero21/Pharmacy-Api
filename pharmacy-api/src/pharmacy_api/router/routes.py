from flask import Blueprint, jsonify, request

# Creamos el Blueprint para el módulo de categorías
categories_bp = Blueprint("categories", __name__)

#categories routes

def create_categories_blueprint(categories_controller):

    @categories_bp.route("/categories", methods=["GET"])
    def list_categories():
        try:
            categories = categories_controller.list_categories()
            return jsonify(categories), 200
        except Exception as e:
            return jsonify({"error": f"Error al obtener categorías: {str(e)}"}), 500

    @categories_bp.route("/categories/<string:code>", methods=["GET"])
    def find_category_by_code(code):
        try:
            category = categories_controller.find_category_by_code(code)
            if not category:
                return jsonify({"error": "Categoría no encontrada"}), 404
            return jsonify(category), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @categories_bp.route("/categories", methods=["POST"])
    def new_category():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            success = categories_controller.new_category(data)
            if not success:
                return jsonify({"error": "La categoría con ese código ya existe"}), 409

            return jsonify({"message": "Categoría creada con éxito"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al crear categoría: {str(e)}"}), 500

    @categories_bp.route("/categories/<string:code>", methods=["PUT"])
    def edit_category(code):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            data["code"] = code

            success = categories_controller.edit_category(data)
            if not success:
                return jsonify({"error": "Categoría no encontrada para actualizar"}), 404

            return jsonify({"message": "Categoría actualizada con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al actualizar categoría: {str(e)}"}), 500

    @categories_bp.route("/categories/<string:code>", methods=["DELETE"])
    def delete_category(code):
        try:
            success = categories_controller.delete_category(code)
            if not success:
                return jsonify({"error": "Categoría no encontrada para eliminar"}), 404

            return jsonify({"message": "Categoría eliminada con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al eliminar categoría: {str(e)}"}), 500

    return categories_bp



employees_bp = Blueprint("employees", __name__)

#employees routes

def create_employees_blueprint(employees_controller):
    @employees_bp.route("/employees", methods=["GET"])
    def list_employees():
        try:
            employees = employees_controller.list_employees()
            return jsonify(employees), 200
        except Exception as e:
            return jsonify({"error": f"Error al obtener empleados: {str(e)}"}), 500

    @employees_bp.route("/employees/<string:username>", methods=["GET"])
    def find_employee_by_username(username):
        try:
            employee = employees_controller.find_employee_by_username(username)
            if not employee:
                return jsonify({"error": "Empleado no encontrado"}), 404
            return jsonify(employee), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @employees_bp.route("/employees", methods=["POST"])
    def create_user():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            success = employees_controller.create_user(data)
            if not success:
                return jsonify({"error": "El usuario con ese username ya existe"}), 409

            return jsonify({"message": "Empleado creado con éxito"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al crear empleado: {str(e)}"}), 500

    @employees_bp.route("/employees/<string:username>", methods=["PUT"])
    def update_user(username):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            data["username"] = username

            success = employees_controller.update_user(data)
            if not success:
                return jsonify({"error": "Empleado no encontrado para actualizar"}), 404

            return jsonify({"message": "Empleado actualizado con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al actualizar empleado: {str(e)}"}), 500

    @employees_bp.route("/employees/<string:username>", methods=["DELETE"])
    def delete_user(username):
        try:
            success = employees_controller.delete_user(username)
            if not success:
                return jsonify({"error": "Empleado no encontrado para eliminar"}), 404

            return jsonify({"message": "Empleado eliminado con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al eliminar empleado: {str(e)}"}), 500

    @employees_bp.route("/employees/<string:username>/password", methods=["PATCH"])
    def change_password(username):
        try:
            data = request.get_json()
            if not data or "new_password" not in data:
                return jsonify({"error": "El campo 'new_password' es obligatorio"}), 400

            success = employees_controller.change_password(username, data["new_password"])
            if not success:
                return jsonify({"error": "Empleado no encontrado para cambiar contraseña"}), 404

            return jsonify({"message": "Contraseña actualizada con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al cambiar contraseña: {str(e)}"}), 500

    return employees_bp

from flask import Blueprint, jsonify, request

medications_bp = Blueprint("medications", __name__)

# medications routes

def create_medications_blueprint(medications_controller):


    @medications_bp.route("/medications", methods=["GET"])
    def get_all_medications():
        try:
            medications = medications_controller.get_all_medications()
            return jsonify(medications), 200
        except Exception as e:
            return jsonify({"error": f"Error al obtener medicamentos: {str(e)}"}), 500

    @medications_bp.route("/medications/<string:name>", methods=["GET"])
    def find_medication_by_name(name):
        try:
            medication = medications_controller.find_medication_by_name(name)
            if not medication:
                return jsonify({"error": "Medicamento no encontrado"}), 404
            return jsonify(medication), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @medications_bp.route("/medications", methods=["POST"])
    def add_medication():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            success = medications_controller.add_medication(data)
            if not success:
                return jsonify({"error": "El medicamento con ese nombre ya existe"}), 409

            return jsonify({"message": "Medicamento agregado con éxito"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al agregar medicamento: {str(e)}"}), 500

    @medications_bp.route("/medications/<string:name>", methods=["PUT"])
    def update_medication(name):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Cuerpo de la petición JSON requerido"}), 400

            # Nos aseguramos de asignar el nombre recibido por la URL
            data["name"] = name

            success = medications_controller.update_medication(data)
            if not success:
                return jsonify({"error": "Medicamento no encontrado para actualizar"}), 404

            return jsonify({"message": "Medicamento actualizado con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al actualizar medicamento: {str(e)}"}), 500

    @medications_bp.route("/medications/<string:name>", methods=["DELETE"])
    def delete_medication(name):
        try:
            success = medications_controller.delete_medication(name)
            if not success:
                return jsonify({"error": "Medicamento no encontrado para eliminar"}), 404

            return jsonify({"message": "Medicamento eliminado con éxito"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error al eliminar medicamento: {str(e)}"}), 500

    return medications_bp
