from pyscript import document


def name():
    user_input= input("Enter your name: ")
    greeting = f'Hello {user_input}! Welcome to the website!'
    return greeting

# Call the function
output = name()

# Print the greeting
def run_program(event):
    print("THIS IS THE TEST")
    output_div = document.querySelector("#output")
    output_div.innerText = output
