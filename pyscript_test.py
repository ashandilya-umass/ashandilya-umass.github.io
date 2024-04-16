from pyscript import document

def run_program():
    # Create an input field
    input_field = document.createElement("input")
    input_field.id = "name"
    input_field.type = "text"
    document.body.appendChild(input_field)
    
    # Create a submit button
    submit_button = document.createElement("button")
    submit_button.id = "submit-btn"
    submit_button.textContent = "Submit"
    document.body.appendChild(submit_button)

    # Create a div for displaying the output
    output_div = document.createElement("div")
    output_div.id = "output"
    document.body.appendChild(output_div)

    # Function to handle the button click
    async def on_submit(event):
        user_input = document.getElementById("name").value
        greeting = f'Hello, {user_input}!'
        output_div.textContent = greeting
    
    # Add event listener to the button
    submit_button.addEventListener("click", on_submit)

run_program()
