from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper Game!")
root.configure(background="#6082B6")

rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))

user_label = Label(root, image=scissor_img, bg="#6082B6")
comp_label = Label(root, image=scissor_img, bg="#6082B6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=('Times', 200, 'bold'), bg="#6082B6", fg="white")
computerScore = Label(root, text=0, font=('Times', 200, 'bold'), bg="#6082B6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, bg="#6082B6", font=('Helvetica', 16, 'bold', 'italic', 'underline'), fg="white", text="USER").grid(row=0, column=3)
computer_indicator = Label(root, bg="#6082B6", font=('Helvetica', 16, 'bold', 'italic', 'underline'), fg="white", text="COMPUTER").grid(row=0, column=1)

msg = Label(root,text="Start Playing!", font=('Helvetica', 16, 'bold'), bg="#6082B6", fg="white", bd=2)
msg.grid(row=3, column=2)

def updateMessage(x, color):
    msg['text'] = x
    msg['fg'] = color

def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore['text'] = str(score)

def checkWin(player, computer):
    if player == computer:
        updateMessage("DRAW!", "white")
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOSE", "red")
            updateCompScore()
        else:
            updateMessage("YOU WON", "green")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("YOU LOSE", "red")
            updateCompScore()
        else:
            updateMessage("YOU WON", "green")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("YOU LOSE", "red")
            updateCompScore()
        else:
            updateMessage("YOU WON", "green")
            updateUserScore()
    else:
        pass

choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)

    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

rock = Button(root, font=('Comic Sans MS', 12), width=20, height=2, text="ROCK", bg="#ca665a", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)

scissor = Button(root, font=('Comic Sans MS', 12), width=20, height=2, text="SCISSOR", bg="#5ab4ca", fg="lightgray", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=2)

paper = Button(root, font=('Comic Sans MS', 12), width=20, height=2, text="PAPER", bg="#b4ca5a", fg="black", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=3)
root.mainloop()
