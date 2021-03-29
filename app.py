#!flask/bin/python
from flask import Flask, jsonify, request, abort
import functions

app = Flask(__name__, static_url_path="")


@app.errorhandler(400)
def bad_request(e):
    """Customize bad request error handler"""
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def not_found(e):
    """Customize not found error handler"""
    return jsonify(error=str(e)), 404


@app.route('/start', methods=['GET'])
def handle_data():
    """Handle data by rule"""
    if request.is_json:
        data = request.json.get('data')
        rule = request.json.get('rule')
        validate_data(data)
        validate_rule(rule)
        return jsonify({'result': execute_sequence(data, rule)})
    abort(400, description="Content-Type is not application/json")


def execute_sequence(data, rule):
    """Execute data according to rule sequence"""
    for func in rule:
        for index, value in enumerate(data):
            func_name = "_".join(["fun", func])
            # run function by name and redefine value of data element
            data[index] = getattr(functions, func_name)(value)
    return data


def validate_data(data):
    """Validate data"""
    for value in data:
        if isinstance(value, (int, float)):
            continue
        abort(400, description="Wrong data value type")


def validate_rule(rule):
    """Validate rule"""
    if len(rule) == 6:
        for func in rule:
            func_name = "_".join(["fun", func])
            if isinstance(func, str) and func_name in functions.SEQUENCE:
                continue
            abort(400, description="Wrong rule value")
    else:
        abort(400, description="Wrong rule length")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
