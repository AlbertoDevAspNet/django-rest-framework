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