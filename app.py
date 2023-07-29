from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to Calculator</h1>"

@app.route('/calc', method = ["GET"])
def math_operator():
    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation == "add":
        result = int(number1) + int(number2)

    elif operation == "sub":
        result = int(number1) - int(number2)

    elif operation == "mul":
        result = int(number1) * int(number2)

    else:
        result = int(number1)/int(number2)

    return "The operation is {} and the result is {}".format(operation, result)

    
    


if __name__ == '__main__':
    app.run()

