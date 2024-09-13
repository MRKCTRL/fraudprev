from flask import Blueprint, request, jsonify
from .models import Payment, TransactionTrail
from . import db 


main=Blueprint('main', __name__)


@main.route('/make_payment', methods=['POST'])
def make_payment():
    data=request.get_json()
    recipient=data.get('recipient')
    amount=float(data.get('amount'))
    description=data.get('description')
    
    
    if not recipient or amount <=0:
        return jsonify({'error': 'invalid input'}), 400
    
    
    payment=Payment(recipient=recipient, amount=amount, description=description)
    db.session.add(payment)
    db.session.commit()
    
    
    transaction=TransactionTrail(payment_id=payment.id, sender='Some User', receiver=recipient, amount=amount)
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({'message': 'Payment made successfuly'}), 201