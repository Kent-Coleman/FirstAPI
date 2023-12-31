from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET']) # End point with GET method
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/user/', methods=['GET']) # Request end point
def request_page():
    user_query = str(request.args.get('user')) # /user/?user=FIAHVSISDAH

    data_set = {'Page': 'Request', 'Message': f'Successfully got the request for {user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777) #Specify port to run on