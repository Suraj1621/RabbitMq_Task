import pika
import json

# RabbitMQ configuration
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = "employee_queue"

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=RABBITMQ_QUEUE)

# Define different types of employee data
employees = [
    {"name": "John Doe", "age": 30, "department": "HR"},
    {"name": "Jane Smith", "age": 35, "department": "Engineering"},
    {"name": "Alice Johnson", "age": 40, "department": "Finance"},
    {"name": "Bob Brown", "age": 25, "department": "Marketing"},
    {"name": "Emma Davis", "age": 28, "department": "Operations"}
]

# Publish each employee data to the queue
for employee in employees:
    channel.basic_publish(exchange="", routing_key=RABBITMQ_QUEUE, body=json.dumps(employee))
    print(f"Employee data sent to RabbitMQ: {employee}")

# Close the connection
connection.close()
