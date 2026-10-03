from flask import Flask
from flask_cors import CORS

from pharmacy_api.router.routes import (
    create_categories_blueprint,
    create_employees_blueprint,
    create_medications_blueprint,
)


def create_app(employee_controller, categories_controller, medications_controller):
    """
    Crea y configura la aplicación Flask inyectando los controladores.
    """
    app = Flask(__name__)
    CORS(app)

    # Registra los Blueprints pasándole a cada fábrica su controlador correspondiente
    app.register_blueprint(
        create_employees_blueprint(employee_controller),
        url_prefix="/api/v1"
    )
    app.register_blueprint(
        create_categories_blueprint(categories_controller),
        url_prefix="/api/v1"
    )
    app.register_blueprint(
        create_medications_blueprint(medications_controller),
        url_prefix="/api/v1"
    )

    return app
