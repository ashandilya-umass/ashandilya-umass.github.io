from pyscript import document
import requests
from bs4 import BeautifulSoup
# import pandas as pd
# import webbrowser
# import rdkit
# from rdkit import Chem
# import plotly.express as px
# from rdkit.Chem.Draw import rdMolDraw2D
# from rdkit import Chem
# import random





def run_program(event):
    website_links = {'alzheimer': "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                 'alzheimers': "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                 'alzheimer\'s': "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                 'alzheimers disease': "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                 'alzheimer\'s disease': "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                 'HIV': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'hiv': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'human immunodeficiency virus': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'aids': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'AIDS': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'AIDs': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'acquired immunodeficiency syndrome': "https://en.wikipedia.org/wiki/HIV/AIDS",
                 'dementia': "https://en.wikipedia.org/wiki/Dementia",
                 'diabetes': "https://en.wikipedia.org/wiki/Diabetes",
                 'depression': "https://en.wikipedia.org/wiki/Depression_(mood)",
                 'anxiety': "https://en.wikipedia.org/wiki/Anxiety",
                 'hemorrhoid': "https://en.wikipedia.org/wiki/Hemorrhoid",
                 'hemerrhoids': "https://en.wikipedia.org/wiki/Hemorrhoid",
                 'yeast infection': "https://en.wikipedia.org/wiki/Candidiasis",
                 'lupus': "https://en.wikipedia.org/wiki/Lupus",
                 'shingles': "https://en.wikipedia.org/wiki/Shingles",
                 'psoriasis': "https://en.wikipedia.org/wiki/Psoriasis",
                 'bronchitis': "https://en.wikipedia.org/wiki/Bronchitis",
                 'pneumonia': "https://en.wikipedia.org/wiki/Pneumonia",
                 'strep': "https://en.wikipedia.org/wiki/Streptococcal_pharyngitis",
                 'strep throat': "https://en.wikipedia.org/wiki/Streptococcal_pharyngitis",
                 'streptococcus pneumonia': "https://en.wikipedia.org/wiki/Streptococcal_pharyngitis",
                 'streptococcus pharyngitis': "https://en.wikipedia.org/wiki/Streptococcal_pharyngitis",
                 'flu': "https://en.wikipedia.org/wiki/Influenza",
                 'the flu': "https://en.wikipedia.org/wiki/Influenza",
                 'influenze': "https://en.wikipedia.org/wiki/Influenza",
                ' hbp': "https://en.wikipedia.org/wiki/Hypertension",
                 'high blood pressure': "https://en.wikipedia.org/wiki/Hypertension",
                 'hypertension': "https://en.wikipedia.org/wiki/Hypertension",
                 'cancer': "https://en.wikipedia.org/wiki/Cancer",
                 'diarrhea': "https://en.wikipedia.org/wiki/Diarrhea",
                 'covid': "https://en.wikipedia.org/wiki/COVID-19",
                 'covid-19': "https://en.wikipedia.org/wiki/COVID-19",
                 'coronavirus': "https://en.wikipedia.org/wiki/COVID-19",
                 'arthritis': "https://en.wikipedia.org/wiki/Arthritis"}

    # word_bank_diseases = ['alzheimer', 'hiv','human immunodeficiency virus','aids',
    #                 'acquired immunodeficiency syndrome','dementia','diabetes','depression','anxiety','hemorrhoid','yeast infection','lupus','shingles',
    #                 'psoriasis','bronchitis','pneumonia','strep','flu', 'hbp',
    #                 'high blood pressure','hypertension','cancer','diarrhea','covid','coronavirus','arthritis']
    # # Get the input field value
    user_input = document.getElementById("name").value
    # user_input = user_input.lower()
    # output = user_input
    # for disease in word_bank_diseases:
    #     if disease in output:
    #         # user_input_split = confirmation(disease)
    #         word = disease
            
    #         url = website_links[word]
    #         response = requests.get(url)

    #         if response.status_code == 200:
    #             soup = BeautifulSoup(response.text, 'html.parser')
    #             title = soup.title.string
    #             output = f'Title: {title}'
    #             soup = BeautifulSoup(response.text, 'html.parser')
    #             paragraphs = soup.find_all('p')
    #             info_text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
    #             output = output + '\n' + info_text + '\n' + f'Website Link: {url}'
    #             # print("Title:", title)
    #         else:
    #             # print("Failed to retrieve the webpage. Status code:", response.status_code)
    #             output = f'Failed to retrieve the webpage. Status code: {response.status_code}'
                
    # output_div = document.getElementById("output")
    # output_div.textContent = output
    
    # def confirmation(word):
    #     while True:
    #         # print(word)

    #         # Ask if the user would like the random structure here, if YES: print it out here, if NO: move on to asking if they want more
    #         # info about their inputted disease

    #         confirm = input(f'Would you like to know more about {word}? (yes or no)')
    #         confirm = confirm.lower()
    #         print(confirm)
    #         if confirm == 'yes':
    #             print(f'Understood, here is some information on {word}: ')

    #             # Outputs the title of the website:
    #             url = website_links[word]
    #             response = requests.get(url)

    #             if response.status_code == 200:
    #                 soup = BeautifulSoup(response.text, 'html.parser')
    #                 title = soup.title.string
    #                 print("Title:", title)
    #             else:
    #                 print("Failed to retrieve the webpage. Status code:", response.status_code)

    #             # Outputs the information on the website:
    #             url = website_links[word]
    #             response = requests.get(url)

    #             if response.status_code == 200:
    #                 soup = BeautifulSoup(response.text, 'html.parser')
    #                 paragraphs = soup.find_all('p')
    #                 info_text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
    #             else:
    #                 print("Failed to retrieve the webpage. Status code:", response.status_code)

    #             window = tk.Tk()
    #             window.title(f"More information on {word}")

    #             # Configure window size
    #             window.geometry("800x600")

    #             # Create a scrolled text area
    #             text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30)
    #             text_area.insert(tk.INSERT, info_text)
    #             text_area.pack(padx=10, pady=10)

    #             # Create a clickable link
    #             link_label = tk.Label(window, text="Click here to visit Wikipedia.com", fg="blue", cursor="hand2")
    #             link_label.pack(pady=10)

    #             link_label.bind("<Button-1>", lambda e: open_link())

    #             window.mainloop()
    #             return word
    #         elif confirm == 'no':
    #             print(f"Got it, thank you for trying us out!")
    #             return "next"
    #         else:
    #             print(f"Enter yes or no")
    # def open_link():
    #     webbrowser.open(website_links[word])
    if user_input != "":
        
        greeting = f'Hello, {user_input}! Welcome to the Website!'
        
        # Display the greeting in the output div
        output_div = document.getElementById("output")
        output_div.textContent = user_input
        output_div.textContent = greeting
        output_div.textContent = website_links[0]

run_program(None)
