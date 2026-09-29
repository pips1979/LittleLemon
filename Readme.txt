Little Lemon - Back-end capstone project (Django REST Framework + MySQL)

SETUP
1. Create and activate a virtual environment, then:
   pip install -r requirements.txt
2. Create a MySQL database named LittleLemon (MySQL 8.0+).
3. In littleLemon/settings.py set DATABASES USER and PASSWORD for your local MySQL.
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver
7. Unit tests: python manage.py test

STATIC HTML PAGE
GET  http://127.0.0.1:8000/restaurant/

USER REGISTRATION AND AUTHENTICATION (Djoser + token)
POST http://127.0.0.1:8000/auth/users/                (body: username, password)
POST http://127.0.0.1:8000/auth/token/login/          (body: username, password) -> auth_token
POST http://127.0.0.1:8000/auth/token/logout/         (header Authorization: Token <token>)
POST http://127.0.0.1:8000/restaurant/api-token-auth/ (body: username, password) -> token
GET  http://127.0.0.1:8000/restaurant/message/        (protected view, needs token)

All protected endpoints need the header:
Authorization: Token <your token>

MENU API
GET  http://127.0.0.1:8000/restaurant/menu/items/     (list)
POST http://127.0.0.1:8000/restaurant/menu/items/     (body JSON: title, price, inventory)
GET/PUT/DELETE http://127.0.0.1:8000/restaurant/menu/items/<id>   (no trailing slash)

TABLE BOOKING API
GET/POST http://127.0.0.1:8000/restaurant/booking/tables/
   (body JSON: name, no_of_guests, booking_date e.g. 2026-10-05T20:00:00)
GET/PUT/DELETE http://127.0.0.1:8000/restaurant/booking/tables/<id>/

ADMIN
http://127.0.0.1:8000/admin/