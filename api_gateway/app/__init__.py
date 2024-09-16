from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import os 
import requests
from flask import Flask, jsonify


db=SQLAlchemy()



def create():
    app=Flask(__name__)
    
    @app.route('/<service>/<path:path>', methods=['GET','POST','PUT'])
    def proxy(service, path):
        if service=='auth':
            target_url=f"http://auth_service:5000/{path}"
        elif service=='payment':
            target_url=f"http://payment_service:5001/{path}"
        elif service =='fraud':
            target_url=f"http://fraud_service:50002/{path}"
        else: 
            return jsonify({'error': 'Service not found'}), 404
        
        response= requests.requests(method=requests.method, url=target_url, json=requests.get_json())
        return jsonify(response.json()), response.status_code
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    
    db.init_app(app)
    CORS(app)
    from .routes import main 
    app.register_blueprint(main)
    
    
    return app

@app.route('/v1/login', methods=['POST'])
def login():
    pass

@app.route('/v2/login', methods=['POST'])
def login_v2():
    pass