from flask import Flask, render_template, jsonify, request, send_file, json


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))


app = CustomFlask(__name__)  # This replaces your existing "app = Flask(__name__)"

data_received = []
received = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/word', methods=['POST', 'GET'])
def word():
    assert request.method == "POST", "POST request expected received {}".format(request.method)
    if request.method == 'POST':
        print(request.json)
        data_received.append(request.json)
        global received
        received = True
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 404, {'ContentType': 'application/json'}


@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    if request.method == 'POST':
        global received
        if received:
            data_to_return = jsonify(data_received[-1])
            received = False
            return data_to_return
        else:
            return jsonify({"0": "__EMPTY"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
