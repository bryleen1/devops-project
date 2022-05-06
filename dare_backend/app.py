from flask import Flask, request, Response 
import random

app = Flask(__name__)

@app.route('/get_dare',methods=['GET'])
def dare(): 
    dare_list = ["Do your best impression of someone in the room and keep going until someone correctly guesses who it is.", 
    "Sing the chorus of your favorite song.", 
    "Describe what the sky looks like without using the words blue or white.", 
    "Make up a song about the player next to you.", 
    "Get down on one knee and propose to the person on your left.",
    "Stand in the backyard and yell at the top of your lungs, “I was adopted! Nooooooo.”" ]
    dare_choice = random.choice(dare_list)
    return Response(f"{dare_choice}", mimetype="text/plain")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)