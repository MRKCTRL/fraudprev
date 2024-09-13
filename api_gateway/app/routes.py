from flask import Blueprint, jsonify
from .models import Payment 


main=Blueprint('main', __name__)


@main.route('/detect_fraud', methods=['GET'])
def detect_fraud():
    sus_payment=Payment.query.filter_by(fraud_alert=True).all()
    return jsonify({'sus_payment': [p.id for p in sus_payment]})