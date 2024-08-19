import tkinter as tk
import random

# Function to handle user choice
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Update labels with the choices and the result
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)

# Set up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x300")

# Labels to display choices and result
user_choice_label = tk.Label(root, text="Your choice: ", font=('Arial', 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=('Arial', 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'))
result_label.pack(pady=20)

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
