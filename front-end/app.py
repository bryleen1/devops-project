from flask import Flask
import requests, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home(): 
    truth_api = requests.get('http://truth_backend:5000/get_truth')
    dare_api = requests.get('http://dare_backend:5000/get_dare')
    return Response(f"{truth_api.text} \n{dare_api.text}", mimetype="text/plain")

# Figure out how to add service four. Maybe in it's own route? Combined backend is a messs

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)