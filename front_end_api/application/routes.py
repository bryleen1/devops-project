from application import app 
from flask import Flask, request, Response, render_template, url_for
import requests, json

"""
 @app.route('/', methods=['GET'])
 def home(): 
     truth_api = requests.get('http://truth_api:5000/get_truth')
     dare_api = requests.get('http://dare_api:5000/get_dare')
    
     content = {'truth': truth_api.text, 'dare': dare_api.text}

     merge_api1 = requests.post('http://merge_api:5000/post/truth', json=content)
     merge_api2 = requests.post('http://merge_api:5000/post/dare', json=content)/
    

     return Response(f"Truth: \t{truth_api.text} \t{merge_api1.text} \nDare: \t{dare_api.text} \t{merge_api2.text}", mimetype="text/plain")
"""

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('main.html')


@app.route('/truth', methods=['POST','GET'])
def truth():
    truth_api = requests.get('http://truth_api:5000/get_truth')
    content = {'truth': truth_api.text}
    merge_api1 = requests.post('http://merge_api:5000/post/truth', json=content)
    statement = truth_api.text 
    merge_msg = merge_api1.text
    return render_template('main.html', statement=statement, merge_msg=merge_msg)


@app.route('/dare', methods=['POST','GET'])
def dare():
    dare_api = requests.get('http://dare_api:5000/get_dare')
    content = {'dare': dare_api.text}
    merge_api2 = requests.post('http://merge_api:5000/post/dare', json=content)
    statement = dare_api.text 
    merge_msg = merge_api2.text
    return render_template('main.html', statement=statement, merge_msg=merge_msg)