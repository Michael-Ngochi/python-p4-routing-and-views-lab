#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return(parameter)

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter))+'\n'
    return result

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1,num2,operator):
    answer=0
    if operator == 'div':
       answer=num1/num2
    elif operator == '+':
        answer=num1+num2
    elif operator == '-':
         answer=num1-num2
    elif operator == '*':
        answer=num1*num2
    elif operator == '%':
        answer=num1%num2
    else:
        return 'Invalid operator'
    return f"{answer}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
