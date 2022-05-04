from flask import Flask
import requests, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home(): 
    truth_api = requests.get('http://truth_backend:5000/get_truth').text
    dare_api = requests.get('http://dare_backend:5000/get_dare').text
    #return Response(f"{truth_api.text} \n{dare_api.text}", mimetype="text/plain")


content = {'truth': 'truth', 'dare': 'dare'}
status = requests.post('http://service-4:5000/post/status', json=content).json()
json_response = status.json()

statement = f"Truth:\t{truth_api} \nDare:\t{dare_api} \n{json_response["truth"]} points for truth \n{json_response["dare"]} points for dare"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)