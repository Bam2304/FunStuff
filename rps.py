import random
import tkinter as tk


choices = ["rock", "paper", "scissors"]


global u_score
global c_score
global games


def initialize():  # start scores off at 0
    global u_score
    u_score = 0
    global c_score
    c_score = 0
    global games
    games = 0


initialize()


def rock_button():
    global games
    if games >= 5 or u_score == 3 or c_score == 3:
        scoreLabel.config(text="Time for a new game. This one's over...")
        outcomeLabel.config(text="")
    else:
        user_choice = "rock"  # set user choice to rock; computer's is random
        comp_choice = random.choice(choices)
        checkWin(user_choice, comp_choice)


def paper_button():
    global games
    if games >= 5 or u_score == 3 or c_score == 3:
        scoreLabel.config(text="Time for a new game. This one's over...")
        outcomeLabel.config(text="")
    else:
        user_choice = "paper"  # sets user choice to paper
        comp_choice = random.choice(choices)
        checkWin(user_choice, comp_choice)


def scissors_button():
    global games
    if games >= 5 or u_score == 3 or c_score == 3:
        scoreLabel.config(text="Time for a new game. This one's over...")
        outcomeLabel.config(text="")
    else:
        user_choice = "scissors"  # sets user choice to scissors
        comp_choice = random.choice(choices)
        checkWin(user_choice, comp_choice)


def reset_button():  # reset scores and number of games
    global u_score
    global c_score
    global games
    u_score = 0
    c_score = 0
    games = 0
    scoreLabel.config(text="Score")
    outcomeLabel.config(text="Outcome")


def checkWin(user, computer):  # compares user choice with computer choice and display result
    global u_score
    global c_score
    global games
    if user == computer:
        outcomeLabel.config(text=f"Computer chose {computer}. It's a draw!")
    elif user == "rock":
        if computer == "scissors":
            outcomeLabel.config(text=f"Computer chose {computer}. You won!")
            u_score += 1
        elif computer == "paper":
            outcomeLabel.config(text=f"Computer chose {computer}. Computer won!")
            c_score += 1
    elif user == "paper":
        if computer == "rock":
            outcomeLabel.config(text=f"Computer chose {computer}. You won!")
            u_score += 1
        elif computer == "scissors":
            outcomeLabel.config(text=f"Computer chose {computer}. Computer won!")
            c_score += 1
    elif user == "scissors":
        if computer == "rock":
            outcomeLabel.config(text=f"Computer chose {computer}. Computer won!")
            c_score += 1
        elif computer == "paper":
            outcomeLabel.config(text=f"Computer chose {computer}. You won!")
            u_score += 1

    scoreLabel.config(text=f"Score is  You: {u_score} | Computer: {c_score}")

    games += 1

    if games == 5 or u_score == 3 or c_score == 3:  # check if the game is over
        scoreLabel.config(text=f"Game Over! The final Score is  You: {u_score} | Computer: {c_score}")


# creating GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("800x800")
root.configure(background="sky blue")

topLabel = tk.Label(root, text="Welcome! Best of 5!", font=('Arial', 30))
topLabel.pack()

scoreLabel = tk.Label(root, text="Score", width=55, height=6, bg="gray", font=('Arial', 25))
scoreLabel.pack()

outcomeLabel = tk.Label(root, text="Outcome", bg="gray", width=40, height=15, font=('Arial', 25))
outcomeLabel.place(x=200, y=300)


image1 = tk.PhotoImage(file='/Users/badeyemo/Downloads/rockImage.png')  # downloaded images
image2 = tk.PhotoImage(file='/Users/badeyemo/Downloads/paperImage.png')
image3 = tk.PhotoImage(file='/Users/badeyemo/Downloads/scissorsImage.png')
image4 = tk.PhotoImage(file='/Users/badeyemo/Downloads/newGameButton2.png')

rockBtn = tk.Button(root, text="", command=rock_button, image=image1, borderwidth=0)
rockBtn.place(x=20, y=300)

paperBtn = tk.Button(root, text="", command=paper_button, image=image2, borderwidth=0)
paperBtn.place(x=20, y=450)

scissorsBtn = tk.Button(root, text="", command=scissors_button, image=image3, borderwidth=0)
scissorsBtn.place(x=20, y=600)

reset = tk.Button(root, text="", command=reset_button, image=image4, borderwidth=0)
reset.pack()

root.mainloop()

















