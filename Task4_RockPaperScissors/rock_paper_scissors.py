import random
from tkinter import *

user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    computer_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"You: {user_score} | Computer: {computer_score}"
    )


root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x350")
root.resizable(False, False)

Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold")
).pack(pady=10)

Button(
    root,
    text="Rock",
    width=15,
    command=lambda: play("Rock")
).pack(pady=5)

Button(
    root,
    text="Paper",
    width=15,
    command=lambda: play("Paper")
).pack(pady=5)

Button(
    root,
    text="Scissors",
    width=15,
    command=lambda: play("Scissors")
).pack(pady=5)

computer_label = Label(
    root,
    text="Computer chose: -",
    font=("Arial", 12)
)

computer_label.pack(pady=10)

result_label = Label(
    root,
    text="Make your move!",
    font=("Arial", 14)
)

result_label.pack(pady=10)

score_label = Label(
    root,
    text="You: 0 | Computer: 0",
    font=("Arial", 12, "bold")
)

score_label.pack(pady=10)

root.mainloop()
