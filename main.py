from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET']) #End point with GET method
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump