import tensorflow as tf 


model=tf.keras.models.load_model('fraud_detection_model')


def predict_fraud(data):
    prediction=model.predict(data)
    return prediction 