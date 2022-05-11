from application import app 
from flask import Flask, request, Response 
import random

truth_list = ["What was the last thing you searched for on your phone web browser?", 
"If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?", 
"If you had to date one of your exs again, who would it be?", 
"What is the most embarrassing situation you’ve ever been a part of?", 
"Do you pee in the shower?", 
"What dumb thing have you done for love?"]

@app.route('/get_truth',methods=['GET'])
def truth(): 
    truth_choice = random.choice(truth_list)
    return Response(f"{truth_choice}", mimetype="text/plain")