import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue = channel.queue_declare('student_report')
queue_name = queue.method.queue

channel.queue_bind(
    exchange='student',
    queue=queue_name,
    routing_key='student.report'
)

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('Generating Report ')
    print(f"""
        ID: {payload.get('id')}
        Student Name: {payload.get('student_name')}
        Student Email: {payload.get('student_email')}
        Education: {payload.get('education')}
    """)
    print('✔️  Done. ')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)
print('✔️ Waiting for Report message. To exit press CTRL + C ')
channel.start_consuming()