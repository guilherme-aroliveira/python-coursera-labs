"""
Flask Server
"""


from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication

# Import the Maths package here

app = Flask("Mathematics Problem Solver")


@app.route("/sum")
def sum_route():
    """
    Method to sum two values
    """
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        # Write your code here
        result = summation(num1, num2)
        return result
    except ValueError:
        print("Please enter a number!!")


@app.route("/sub")
def sub_route():
    """
    Method to subtract two values
    """
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = subtraction(num1, num2)
    return result


@app.route("/mul")
def mul_route():
    """
    Method to multiply two values
    """
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = multiplication(num1, num2)
    return result


@app.route("/")
def render_index_page():
    """
    Method to render the index page
    """
    # Write your code here
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
