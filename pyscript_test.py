from pyscript import document

def run_program():
    # Create an input field
    input_field = document.createElement("input")
    input_field.placeholder = "Enter your name"
    document.body.appendChild(input_field)
    
    # Create a button to submit the input
    submit_button = document.createElement("button")
    submit_button.textContent = "Submit"
    document.body.appendChild(submit_button)
    
    # Function to handle the button click
    def on_submit(event):
        user_input = input_field.value
        greeting = f'Hello {user_input}! Welcome to the website!'
        
        # Display the greeting in the browser
        output_div = document.createElement("div")
        output_div.textContent = greeting
        document.body.appendChild(output_div)
        
        # Remove the input field and button
        document.body.removeChild(input_field)
        document.body.removeChild(submit_button)
    
    # Add event listener to the button
    submit_button.addEventListener("click", on_submit)

# Call the function
run_program()
