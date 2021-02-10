# shopbridgebackendrepo
required libraires
1) django-cors-headers
2)django restframework
3)py-mysql

Steps to run shopbridge
-----------------------
1)Install required libraries using pip command
2) Create a shopbridge db in your my sql workbench
3)run migrations
4)run server using python manage.py runserver

Restapi calls

Create
 POST http://localhost:8000/api/inventory

Update

PUT http://localhost:8000/api/inventory/:id

List

GET http://localhost:8000/api/inventory

Delete

DELETE http://localhost:8000/api/inventory/:id

View in Detail

GET http://localhost:8000/api/inventory/:id

Parameters

name,
description,
price
