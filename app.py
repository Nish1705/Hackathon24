from flask import Flask,request,redirect,url_for, render_template,flash,session,jsonify
from flask_mysqldb import MySQL
import time
import pyttsx3
from threading import Lock
from threading import Thread
import final_feature


app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] ='user'
# app.config['SECRET_KEY']='mykey'
# mysql = MySQL(app=app)
threads = []
l = []
# Initialize the engine globally

def t2s(s):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(s)
    try:
        engine.runAndWait()

    except(Exception):
        pass

    engine.stop()

        
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "August", "September", "Oct", "Nov", "Dec"]


# @app.route('/', methods=['POST', 'GET'])
# def home():
#     return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html',month_list = months)



@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    final_feature.final_feat(data)

    

    # Process the data as needed
    result = {'message': 'Data received successfully'}
    
    return jsonify(result)

























if __name__ == '__main__':
    app.run(debug = True)