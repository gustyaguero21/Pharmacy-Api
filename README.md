💊 Pharmacy API

API RESTful para la gestión integral de farmacias, categorías, medicamentos y personal.

👥 Integrantes

Gustavo Aguero

Juan Molina

📝 Descripción

Pharmacy API es el servicio backend que impulsa la plataforma de administración de farmacias. Proporciona una interfaz robusta y escalable para registrar, consultar y gestionar la información esencial del negocio:

🗂️ Categorías: Clasificación y organización de productos.

💊 Medicamentos: Control de inventario y detalles de catálogo.

👥 Empleados: Gestión del personal administrativo y operativo.

🛠️ Tecnologías Utilizadas

Tecnología

Descripción

Python

Lenguaje principal de desarrollo

Flask

Framework web para la construcción de la API REST

MySQL

Sistema de gestión de base de datos relacional

UV

Administrador rápido de paquetes y entornos virtuales de Python

⚙️ Requisitos Previos

Asegúrate de contar con las siguientes herramientas instaladas en tu sistema:

Python (versión recomendada 3.12+)

MySQL Server

Gestor de paquetes UV

🚀 Instalación y Configuración

1. Clonar el repositorio e instalar dependencias

Sincroniza y crea el entorno virtual automáticamente con uv:

uv sync


2. Variables de Entorno

Crea un archivo .env en la raíz del proyecto y configura tus credenciales de MySQL:

DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=pharmacy_api


Nota: La base de datos y la migración de las tablas se crean de manera automática al iniciar la aplicación por primera vez.

🏃 Ejecuciōn del Proyecto

Para iniciar el servidor backend en modo desarrollo, ejecuta:

uv run main.py


(Si el punto de entrada está en el paquete principal, utiliza uv run src/pharmacy_api/main.py)

📁 Estructura del Proyecto

El código está organizado siguiendo un patrón modular y capas bien definidas:

pharmacy-api/
├── 📁 config/             # Configuración general, variables y migraciones
│   ├── env.py
│   ├── migrations.py
│   └── queries.py
├── 📁 controllers/        # Controladores de la API (manejo de peticiones)
│   ├── categories.py
│   ├── employees.py
│   └── medications.py
├── 📁 database/           # Conexión a la base de datos
│   └── database.py
├── 📁 models/             # Modelos de datos
│   ├── categories.py
│   ├── employees.py
│   └── medications.py
├── 📁 repositories/       # Capa de acceso a datos / consultas
│   ├── categories.py
│   ├── employees.py
│   └── medications.py
├── 📁 router/             # Definición e inicialización de rutas
│   ├── routes.py
│   └── server.py
├── 📁 services/           # Lógica de negocio
│   ├── categories.py
│   ├── employees.py
│   └── medications.py
├── 📄 .env                # Configuración local
└── 📄 main.py              # Punto de entrada de la aplicación


🌐 Frontend

El cliente web de la plataforma se gestiona en un repositorio independiente. Asegúrate de configurar e iniciar el proyecto frontend para interactuar de forma gráfica con esta API.

🤝 Distribución de Tareas

Gustavo Aguero

🛠️ Diseño y configuración de la arquitectura del backend.

🔌 Implementación de endpoints RESTful (Categorías, Empleados y Medicamentos).

🧪 Desarrollo de pruebas unitarias.

Juan Molina

🎨 Diseño y configuración de la interfaz del frontend.

🧩 Implementación de componentes de usuario.

🔗 Integración del cliente con la API.
