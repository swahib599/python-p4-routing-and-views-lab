#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Root route for index
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. /print/<parameter> route
@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)  # Print to console
    return parameter

# 3. /count/<parameter> route
@app.route('/count/<int:parameter>')
def count_route(parameter):
    # Return a count from 0 to parameter-1, each on a new line
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

# 4. /math/<num1>/<operation>/<num2> route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Operation not supported", 400
    return str(result)

# Run the app if called directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
