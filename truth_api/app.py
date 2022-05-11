from flask import Flask, request, Response 
import random

app = Flask(__name__)

<<<<<<< HEAD:truth_backend/app.py
@app.route('/get_truth',methods=['GET'])
def truth(): 
    truth_list = ["What was the last thing you searched for on your phone web browser?", 
    "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?", 
    "If you had to date one of your exs again, who would it be?", 
    "What is the most embarrassing situation you’ve ever been a part of?", 
    "Do you pee in the shower?", 
    "What dumb thing have you done for love?"]
    truth_choice = random.choice(truth_list)
    return Response(f"{truth_choice}", mimetype="text/plain")
=======

@app.route('/post/points', methods=['POST'])
def post_points():
    truth = request.json['truth']
    dare = request.json['dare']

    if truth == "What was the last thing you searched for on your phone web browser?":
        points = 2
    elif truth == "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?":
        points = 3
    elif truth == "If you had to date one of your exs again, who would it be?":
        points = 5
    elif truth == "What is the most embarrassing situation you\’ve ever been a part of?":
        points = 7
    elif truth == "Do you pee in the shower?":
        points = 5
    else:
        points = 4

    if dare == "Do your best impression of someone in the room and keep going until someone correctly guesses who it is.":
        points = 6
    elif dare == "Sing the chorus of your favorite song.":
        points = 5
    elif dare == "Describe what the sky looks like without using the words blue or white.":
        points = 7
    elif dare == "Make up a song about the player next to you.":
        points = 8
    elif dare == "Get down on one knee and propose to the person on your left.":
        points = 4
    else:
        points = 7

    points = {"points": points}

    return jsonify(points)


>>>>>>> service_4:combined_backend/app.py

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)