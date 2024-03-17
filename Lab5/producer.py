# Импортируем библиотеку pika
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

message = input("Введите сообщение: ")

channel.basic_publish(exchange='', routing_key='hello', body=message)

print(" [x] Sent '%s'" % message)

connection.close()

