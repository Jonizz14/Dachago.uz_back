# Dachago.uz Backend API

This is the backend for the **Dachago.uz** project, built using **Django** and **Django Rest Framework (DRF)**. It features a robust API with JWT authentication, a product catalog, a blog system, and user management.

## 🚀 Features

-   **JWT Authentication**: Secure login and token-based access using `djangorestframework-simplejwt`.
-   **Product Catalog**: API for managing products with titles, photos, prices, and descriptions.
-   **Blog System**: API for publishing blog posts with photos and descriptions.
-   **User Management**: RESTful endpoints for user listing and deletion (restricted to admins).
-   **Interactive API Docs**: Built-in Swagger UI and Redoc via `drf-spectacular`.
-   **Media Handling**: Automated image upload handling for products and blogs.

## 🛠 Technologies

-   **Backend**: [Django 6.0](https://www.djangoproject.com/)
-   **API Framework**: [Django Rest Framework](https://www.django-rest-framework.org/)
-   **Authentication**: [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)
-   **Documentation**: [drf-spectacular](https://drf-spectacular.readthedocs.io/)
-   **Database**: SQLite (default, easily switchable to PostgreSQL)

## 📋 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Jonizz14/Dachago.uz_back.git
    cd Dachago.uz_back
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies**:
    ```bash
    pip install django djangorestframework drf-spectacular Pillow djangorestframework-simplejwt
    ```

4.  **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the server**:
    ```bash
    python manage.py runserver
    ```

## 📡 API Endpoints

### Authentication
-   `POST /api/token/` - Get access and refresh tokens (Login).
-   `POST /api/token/refresh/` - Refresh expired access token.

### Business Logic
-   `GET/POST /api/products/` - Manage products (Requires Authentication).
-   `GET/POST /api/blogs/` - Manage blog posts.

### User Management
-   `GET /api/users/` - List users (Requires Authentication).
-   `DELETE /api/users/{id}/` - Delete a user (Admin only).

## 📄 Documentation

Once the server is running, you can access the interactive documentation at:
-   **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
-   **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)

## 📝 Admin Panel

The Django Admin panel is available at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
Created and maintained by [Joniz](https://github.com/Jonizz14).
