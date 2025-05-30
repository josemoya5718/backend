# 🧠 Enigma ERP - Backend

Este es el backend del sistema **Enigma**, un ERP modular desarrollado con Django y Django REST Framework. Gestiona productos, equipos, remitos, órdenes de reparación, logística y stock.

---

## 🚀 Requisitos

- Python 3.11 o superior
- Git (opcional, para clonar)
- Pip
- Virtualenv (opcional, pero recomendado)

---

## 📦 Instalación

### 1. Clonar el repositorio (si aplica)

    git clone https://github.com/tu_usuario/backend.git

    cd backend

⚠️ Si descargaste como ZIP, simplemente descomprimí y navegá a la carpeta raíz del proyecto.

### 2. Crear un entorno virtual

    python -m venv env

### 3. Activar el entorno virtual

En Windows (PowerShell):

    .\env\Scripts\activate

En Linux / macOS:

    source env/bin/activate

### 4. Instalar las dependencias

    pip install -r requirements.txt

### 5. Aplicar migraciones

    python manage.py migrate

### 6. Levantar el servidor

    python manage.py runserver

## 🧪 Rutas de prueba (Views básicas por módulo)

Ya que no hay una vista principal (/), podés testear que cada módulo funcione con las siguientes rutas:

| Módulo     | Ruta                                                | Descripción                         |
|------------|-----------------------------------------------------|-------------------------------------|
| Usuarios   | http://localhost:8000/api/usuarios/test/            | Test de usuarios                    |
| Depósitos  | http://localhost:8000/api/depositos/test/           | Test de depósitos y stock           |
| Productos  | http://localhost:8000/api/productos/test/           | Test de productos y equipos         |
| Remitos    | http://localhost:8000/api/remitos/test/             | Test de remitos                     |
| Órdenes    | http://localhost:8000/api/ordenes/test/             | Test de órdenes de revisión         |
| Logística  | http://localhost:8000/api/logistica/test/           | Test de pallets y destinos          |

## 📂 Estructura del proyecto

    enigma/
    ├── apps/
    │   ├── usuarios/
    │   ├── depositos/
    │   ├── productos/
    │   ├── remitos/
    │   ├── ordenes/
    │   └── logistica/
    ├── config/              # Configuración global del proyecto
    ├── manage.py
    └── requirements.txt
