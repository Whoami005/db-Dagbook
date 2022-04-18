from django.http import HttpResponse
from django.shortcuts import render


def index_author(request):
    return HttpResponse('''
    Instruction:
    1) Сreate migrations. Using the command: "python manage.py makemigrations" and "python manage.py migrate"
    2) Create a super user using the command: "python manage.py createsuperuser".
    3) Go to the address: http://127.0.0.1:8000/admin/  to enter the admin panel
    ''')
