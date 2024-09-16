import pika 
import json 


def publish_payment_event(payment_data):
    """Publish a payment event to RabbitMQ when a payment is processed."""
    connection=pika.BlockConnection(pika.ConnectionParameters(host='rabbit'))
    channel=connection.channnel()
    
    channel.queue_declare(queue='payment_queue')
    
    
    
    channel.basic_publish(
        exchange='',
        routing_key='payment_queue',
        body=json.dumps(payment_data)
    )
    
    connection.close()
    
def proccess_payment(user_id, amount):
    
    
    
    payment_data={
        "user_id":user_id,
        'amount':amount,
        'status':'success'
    }
    
    publish_payment_event(payment_data)