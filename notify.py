import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue = channel.queue_declare('student_notify')
queue_name = queue.method.queue

channel.queue_bind(
    exchange='student',
    queue=queue_name,
    routing_key='student.notify'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('Notifying {}'.format(payload['student_email']))
    print('✔️ Received Successfully. ')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)
print('✔️ Waiting for notifying message. To exit press CTRL + C ')
channel.start_consuming()