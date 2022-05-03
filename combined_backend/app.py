from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/post/points', methods=['POST'])
def post_status():
    truth = request.json['truth']
    dare = request.json['dare']

    truth_list = ["What was the last thing you searched for on your phone web browser?", 
    "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?", 
    "If you had to date one of your exs again, who would it be?", 
    "What is the most embarrassing situation you’ve ever been a part of?", 
    "Do you pee in the shower?", 
    "What dumb thing have you done for love?"]

    if truth in truth_list:
        points = 5
    else:
        points = 10



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)