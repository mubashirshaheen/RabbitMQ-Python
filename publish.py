import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='student',
    exchange_type='direct'
)

student = {
    'id': str(uuid.uuid4()),
    'student_name': 'Mubashir Shaheen',
    'student_email': 'test@gmail.com',
    'education': 'BSIT'
}

channel.basic_publish(
    exchange='student',
    routing_key='student.notify',
    body=json.dumps({'student_email': student['student_email']})
)

print('✔️   Sent Notification Successfully. ')

channel.basic_publish(
    exchange='student',
    routing_key='student.report',
    body=json.dumps(student)
)

print('✔️   Sent Report Successfully. ')

connection.close
