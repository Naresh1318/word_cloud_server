import os
import time
import pickle
from flask import Flask, render_template, jsonify, request, json


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))


app = CustomFlask(__name__)  # This replaces your existing "app = Flask(__name__)"

received = False
database_path = "./database.pkl"

if not os.path.exists(database_path):
    with open(database_path, "wb") as file:
        pickle.dump([], file)


def add_data(data):
    with open(database_path, "rb") as file:
        data_received = pickle.load(file)

    with open(database_path, "wb") as file:
        data_received.append(data)
        pickle.dump(data_received, file)


def return_latest():
    with open(database_path, "rb") as file:
        data_received = pickle.load(file)
    if len(data_received) > 0:
        return data_received[-1]
    else:
        return None


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/word', methods=['POST', 'GET'])
def word():
    assert request.method == "POST", "POST request expected received {}".format(request.method)
    if request.method == 'POST':
        data_received = request.json
        data_received["timestamp"] = time.time()
        print(data_received)
        add_data(data_received)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 404, {'ContentType': 'application/json'}


@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    if request.method == 'POST':
        data_to_return = return_latest()
        if not data_to_return:
            return jsonify({"0": "__EMPTY"})
        return jsonify(data_to_return)


@app.route('/reset', methods=["GET"])
def reset():
    with open(database_path, "wb") as file:
        pickle.dump([], file)
    return jsonify({"reset": True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
