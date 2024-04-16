from pyscript import document

def run_program(event):
    # Get the input field value
    user_input = document.getElementById("name").value
    if user_input != "":
        greeting = f'Hello, {user_input}! Welcome to the Website!'
        
        # Display the greeting in the output div
        output_div = document.getElementById("output")
        output_div.textContent = greeting

run_program(None)
