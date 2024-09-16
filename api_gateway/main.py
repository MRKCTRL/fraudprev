import pika 
import json

import sys 
import loguru import logger

def consume_payment():
    """Consume payment events from RabbitMQ and perfom fraud detection."""
    connection=pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel=connection.channel()
    
    
    channel.queue_declare(queue='payment_queue')
    
    def callback(ch, method, properties, body ):
        payment_data=json.loads(body)
        print(f"Received payment data: {payment_data}")
        
        perfrom_fraud_check(payment_data)
        
    
    channel.basic_consume(queue='payment_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    
    
def perform_fraud_check(payment_data):
    """Placeholder for fraud detection."""
    user_id=payment_data['user_id']
    amount=payment_data['amount']
    
    
    print(f"check fraud for payment: {user_id} - {amount}")
    
    
logger.add(sys.stdout,format="{time} {level} {message}", filter="my module", level="INFO", serialize=True)


logger.info("service started")