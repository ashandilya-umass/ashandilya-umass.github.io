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
    submit_button.addEventListener("click", lambda event: on_submit(event))

# Call the function
run_program()


    

# from pyscript import document


# def drug(name='Aducanumab'):
#     #name = input("Enter your name: ")
#     return name

# # Call the function
# output = drug()

# # Print the greeting
# def run_program(event):
#     output_div = document.querySelector("#output")
#     output_div.innerText = output
    
    
