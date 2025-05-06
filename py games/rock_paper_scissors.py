import random
import tkinter as tk

options = ["rock", "paper", "scissors"]

def play(player_choice):
    computer_choice = random.choice(options)
    
    result = ""
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Rock Paper Scissors")
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 16))
label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play("rock"))
paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play("paper"))
scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play("scissors"))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

window.mainloop()