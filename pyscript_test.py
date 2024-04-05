#Using Flask:
#from flask import Flask, render_template
#
#app = Flask(__name__)
#
#@app.route('/')
#def home():
#    return 'Hello, World!'
#
#@app.route('/about')
#def about():
#    return 'This is the about page'
#
#if __name__ == '__main__':
#    app.run(debug=True)


#Using Pyscript?:
from pyscript import document


def greet_person(name='cole'):
    #name = input("Enter your name: ")
    return f"Hello, {name}!"

# Call the function
greeting = greet_person()

# Print the greeting
def run_program(event):
    output_div = document.querySelector("#output")
    output_div.innerText = greeting