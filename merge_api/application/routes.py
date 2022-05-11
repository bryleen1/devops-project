from flask import Flask, request, Response
from application import app
import random


@app.route('/post/truth', methods=['POST'])
def truth():
    truth = request.get_json()["truth"]
    return Response(f"Points randomly generated for this choice: {random.randint(3, 7)}", mimetype = "text/plain")

@app.route('/post/dare', methods=['POST'])
def dare():
    dare = request.get_json()["dare"]
    return Response(f"Points randomly generated for this choice: {random.randint(5, 10)}", mimetype = "text/plain")

