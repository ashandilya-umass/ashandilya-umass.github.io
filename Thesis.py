#Ashwin Shandilya
#University of Massachusetts Amherst Commonwealth Honors College

from pyscript import document
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import rdkit
from rdkit import Chem
import plotly.express as px
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Chem
import random
from Functional_Groups_Output import alz_unique_found_groups
from Functional_Groups_Output import hiv_unique_found_groups
from Functional_Groups_Output import dementia_unique_found_groups
from Functional_Groups_Output import diabetes_unique_found_groups
from Functional_Groups_Output import depression_unique_found_groups
from Functional_Groups_Output import anxiety_unique_found_groups
from Functional_Groups_Output import hemerrhoids_unique_found_groups
from Functional_Groups_Output import yeast_infection_unique_found_groups
from Functional_Groups_Output import lupus_unique_found_groups
from Functional_Groups_Output import shingles_unique_found_groups
from Functional_Groups_Output import psoriasis_unique_found_groups
from Functional_Groups_Output import bronchitis_unique_found_groups
from Functional_Groups_Output import pneumonia_unique_found_groups
from Functional_Groups_Output import strep_unique_found_groups
from Functional_Groups_Output import flu_unique_found_groups
from Functional_Groups_Output import hbp_unique_found_groups
from Functional_Groups_Output import cancer_unique_found_groups
from Functional_Groups_Output import diarrhea_unique_found_groups
from Functional_Groups_Output import covid_unique_found_groups
from Functional_Groups_Output import arthritis_unique_found_groups

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


def open_link():
    webbrowser.open(website_links[word])


def confirmation(word):
    while True:        
        confirm = input(f'Would you like to know more about {word}? (yes or no)')
        confirm = confirm.lower()
        print(confirm)
        if confirm == 'yes':
            print(f'Understood, here is some information on {word}: ')
            url = website_links[word]
            response = requests.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string
                print("Title:", title)
            else:
                print("Failed to retrieve the webpage. Status code:", response.status_code)

            url = website_links[word]
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                info_text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
            else:
                print("Failed to retrieve the webpage. Status code:", response.status_code)
            
            window = tk.Tk()
            window.title(f"More information on {word}")
            
            window.geometry("800x600")

            text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30)
            text_area.insert(tk.INSERT, info_text)
            text_area.pack(padx=10, pady=10)

            link_label = tk.Label(window, text="Click here to visit Wikipedia.com", fg="blue", cursor="hand2")
            link_label.pack(pady=10)

            link_label.bind("<Button-1>", lambda e: open_link())

            window.mainloop()
            return word
        elif confirm == 'no':
            print(f"Got it, thank you for trying us out!")
            return "next"
        else:
            print(f"Enter yes or no")

word_bank_diseases = ['alzheimer', 'hiv','human immunodeficiency virus','aids',
                 'acquired immunodeficiency syndrome','dementia','diabetes','depression','anxiety','hemorrhoid','yeast infection','lupus','shingles',
                 'psoriasis','bronchitis','pneumonia','strep','flu', 'hbp',
                 'high blood pressure','hypertension','cancer','diarrhea','covid','coronavirus','arthritis']


user_input_split = ""
word = ""

user_input = input("What medical function do you want this drug to have?")
if user_input.lower()!="quit":
    user_input = user_input.lower()
    for disease in word_bank_diseases:
        if disease in user_input:
            user_input_split = confirmation(disease)
            word = disease

if word in website_links:
    print(f"More information on {word}: {website_links[word]}")
else:
    print(f"{word} not found in the dictionary.")

print("Have a good day")

def grab_random_functional_groups(inputted_list):
    count=0
    grabbed_random_functional_groups = []
    while count < 5:
        random_choice = random.choice(inputted_list)
        grabbed_random_functional_groups.append(random_choice)
        count +=1
    smile_code = grabbed_random_functional_groups[0]+grabbed_random_functional_groups[1]+grabbed_random_functional_groups[2]+grabbed_random_functional_groups[3]+grabbed_random_functional_groups[4]
    return smile_code

random_generation = {'alzheimer': alz_unique_found_groups,
                 'hiv': hiv_unique_found_groups,
                 'human immunodeficiency virus': hiv_unique_found_groups,
                 'aids': hiv_unique_found_groups,
                 'acquired immunodeficiency syndrome': hiv_unique_found_groups,
                 'dementia': dementia_unique_found_groups,
                 'diabetes': diabetes_unique_found_groups,
                 'depression': depression_unique_found_groups,
                 'anxiety': anxiety_unique_found_groups,
                 'hemorrhoid': hemerrhoids_unique_found_groups,
                 'yeast infection': yeast_infection_unique_found_groups,
                 'lupus': lupus_unique_found_groups,
                 'shingles': shingles_unique_found_groups,
                 'psoriasis': psoriasis_unique_found_groups,
                 'bronchitis': bronchitis_unique_found_groups,
                 'pneumonia': pneumonia_unique_found_groups,
                 'strep': strep_unique_found_groups,
                 'flu': flu_unique_found_groups,
                 'influenze': flu_unique_found_groups,
                ' hbp': hbp_unique_found_groups,
                 'high blood pressure': hbp_unique_found_groups,
                 'hypertension': hbp_unique_found_groups,
                 'cancer': cancer_unique_found_groups,
                 'diarrhea': diarrhea_unique_found_groups,
                 'covid': covid_unique_found_groups,
                 'coronavirus': covid_unique_found_groups,
                 'arthritis': arthritis_unique_found_groups}


letter_to_count = ['C','c','N','n','O','o','S','s']
count = 0
smile_code = grab_random_functional_groups(random_generation[word])
for letter in smile_code:
    if letter in letter_to_count:
        count += 1
print(count)
atom_count=[]
for i in range(0, count):
    atom_count.append(i)
print(atom_count)


mol = Chem.MolFromSmiles(smile_code)

d = rdMolDraw2D.MolDraw2DCairo(300, 300)

s = d.drawOptions()
s.addAtomIndices = True
s.bondLineWidth = 6

d.DrawMolecule(mol)
d.FinishDrawing()
p = d.GetDrawingText()
from matplotlib.colors import *
img = rdkit.Chem.Draw.MolToImage(mol,highlightAtoms=atom_count,highlightColor=ColorConverter().to_rgb('aqua'))

img.show("practice.png")

import IPython.display
i = IPython.display.Image(p)
IPython.display.display(i)

