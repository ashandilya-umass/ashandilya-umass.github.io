from pyscript import document


def drug(name='Aducanumab'):
    #name = input("Enter your name: ")
    return name

# Call the function
output = drug()

# Print the greeting
def run_program(event):
    output_div = document.querySelector("#output")
    output_div.innerText = output
