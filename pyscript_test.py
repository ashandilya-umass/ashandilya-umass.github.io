from pyscript import document

def run_program():
    # Get the input field value
    user_input = document.getElementById("name").value
    greeting = f'Hello, {user_input}!'
    
    # Display the greeting in the output div
    output_div = document.getElementById("output")
    output_div.textContent = greeting

run_program()
