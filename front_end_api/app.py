from flask import Flask
import requests, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home(): 
    truth_api = requests.get('http://truth_backend:5000/get_truth').text
    dare_api = requests.get('http://dare_backend:5000/get_dare').text
    return Response(f"Truth: \t{truth_api.text} \nDare: \t{dare_api.text}", mimetype="text/plain")


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)