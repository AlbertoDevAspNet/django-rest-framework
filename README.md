# django-rest-framework

# cria diretório do projeto
mkdir certificates
cd certificates

# cria a ativa a venv
python3 -m venv venv
source venv/bin/activate

# atualiza pip da venv
python -m pip install --upgrade pip

# instala django e drf
pip install django djangorestframework

# inicializa o projeto django
django-admin startproject core .

# cria o banco de dados do projeto
python manage.py migrate

# cria um super usuário do django
python manage.py createsuperuser

# sobe a api
python manage.py runserver

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
]

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/certificate/', views.CertificateView.as_view(), name='certificate'),
]

from rest_framework import views, response, status

from .tasks import generate_certificate, send_notification, update_student


class CertificateView(views.APIView):

    def post(self, request):
        data = request.data

        generate_certificate(data)
        send_notification(data)
        update_student(data)

        return response.Response(
            data={
                'status': 'ok',
                'message': 'Certificado gerado e enviado.',
                'data': data,
            },
            status=status.HTTP_201_CREATED,
        )

        import time


def generate_certificate(data):
    name = data.get('name')
    email = data.get('email')
    course = data.get('course')
    time.sleep(5)
    print(f'Certificado gerado: {name} - {email} - {course}')

def send_notification(data):
    name = data.get('name')
    email = data.get('email')
    time.sleep(3)
    print(f'Notificação enviada: {name} - {email}')

def update_student(data):
    name = data.get('name')
    email = data.get('email')
    status = 'concluído'
    time.sleep(2)
    print(f'Aluno atualizado: {name} - {email} - {status}')

    
