import tkinter as tk
import random

# Define the Thai consonants and their names
consonants = [
    ("ก", "gor kai"), ("ข", "khor khai"), ("ฃ", "khor khuat"),
    ("ค", "khor khon"), ("ฅ", "khor raakhang"), ("ฆ", "khor khwair"),
    ("ง", "ngor ngu"), ("จ", "jor jaan"), ("ฉ", "chor ching"),
    ("ช", "chor chang"), ("ซ", "sor so"), ("ฌ", "chor choo"),
    ("ญ", "yor ying"), ("ฎ", "dor cha-da"), ("ฏ", "tor tuk"),
    ("ฐ", "thor thung"), ("ฑ", "thor thahaan"), ("ฒ", "thor montho"),
    ("ณ", "nor nen"), ("ด", "dor dek"), ("ต", "tor tao"),
    ("ถ", "thor thung"), ("ท", "thor thaang"), ("ธ", "thor tham"),
    ("น", "nor nooa"), ("บ", "bor bai mai"), ("ป", "por phueng"),
    ("ผ", "phor phum"), ("ฝ", "for fang"), ("พ", "phor phu"),
    ("ฟ", "for fa"), ("ภ", "phor phin"), ("ม", "mor ma"),
    ("ย", "yor yak"), ("ร", "ror raa"), ("ล", "lor ling"),
    ("ว", "wor waen"), ("ศ", "sor sua"), ("ษ", "sor ruu"),
    ("ส", "sor san"), ("ห", "hor he"), ("ฬ", "lor jula"),
    ("อ", "or ang"), ("ฮ", "hor hok")
]

# Function to shuffle and update the card
def flip_card():
    consonant, name = random.choice(consonants)
    # Display the consonant on the front side
    if card_label["text"] == consonant:
        card_label.config(text=name)  # Show the name on the back side
        flip_button.config(text="Next Card")
    else:
        card_label.config(text=consonant)  # Show the consonant on the front side
        flip_button.config(text="Flip Card")

# Setting up the main Tkinter window
root = tk.Tk()
root.title("Thai Consonant Flashcard Game")
root.geometry("400x300")

# Create a label to show the consonant
card_label = tk.Label(root, text="", font=("Helvetica", 48), width=10, height=5, relief="solid")
card_label.pack(pady=50)

# Create a button to flip the card
flip_button = tk.Button(root, text="Flip Card", font=("Helvetica", 14), command=flip_card)
flip_button.pack()

# Initial card display (show a random consonant)
flip_card()

# Start the main loop
root.mainloop()
