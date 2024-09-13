from Flask import Blueprint, request, jsonify
from .models import User
from . import db, bcrypt
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


main=Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
   data=request.get_json() 
   username=data.get('email')
   password=data.get('password')
   email=data.get('email')
   
   if not username or not email or not password: 
      return jsonify({'error': 'all fields are required'})
   
   
   hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
   
   
   new_user=User(username=username, email=email,password=hashed_password)
   db.session.add(new_user)
   db.session.commit()
   return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
   data=request.get_json()
   email=data.get('email')
   password=data.get('password')

   user=User.query.filter_by(email=email).first()
   if user and check_password_hash(user, password):
      login_user(user)
      return jsonify({'message': 'Login successful'}), 200
   return jsonify({'error': 'invalid credentials'}), 404
   
