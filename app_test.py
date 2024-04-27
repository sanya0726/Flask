from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/Sanya')
def hello_world():
   return 'Hello World from Sanya'

@app.route('/datetime')
def get_current_datetime():
   return f'{datetime.now()}'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)


