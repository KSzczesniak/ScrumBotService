from flask import Flask, jsonify, request
from flask_cors import CORS
from chatbot import respond
# from gender import isFemale

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"

@app.route('/chat1', methods=['GET'])
def chat1():
    result = {
        'state': 1,
        'message': 1,
        'params': 1,
        'suggestion': 1,
        'actions': 1
    }
    return jsonify(result)

@app.route('/chat', methods=['POST'])
def chat():
    request_data = request.get_json()
    message = request_data['message']
    state = request_data['state']
    params = request_data['params']
    suggestion = request_data['suggestion']
    actions = request_data['actions']
    new_state, response, params, suggestion, actions = respond(state, message, params, suggestion, actions)
    result = {
        'state': new_state,
        'message': response,
        'params': params,
        'suggestion': suggestion,
        'actions': actions
    }
    return jsonify(result)

@app.route('/gender', methods=['POST'])
def gender():
    request_data = request.get_json()
    firstname = request_data['firstname']
    result = isFemale(firstname)
    return jsonify(result)


app.run(port=5000)
