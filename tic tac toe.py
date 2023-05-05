from tkinter import *
import random


root = Tk()
root.title('Tic Tac Toe Powered by Issa')
game_run = True
field = []
cross_count = 0
scores = {'X': 0, 'O': 0}
history = []

def new_game():
    global game_run, cross_count
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'brown'
    game_run = True
    cross_count = 0

def check_win(smb):
    global game_run
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def click(row, col):
    global cross_count
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def update_score():
    score_label.config(text=f"X: {scores['X']}  O: {scores['O']}")
score_label = Label(root, text="X: 0 O: 0", relief=RIDGE, font=("Arial Black", 12))
score_label.grid(row=4, column=0, columnspan=3)


def check_line(a1, a2, a3, smb):
    global game_run, scores
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'red'
        game_run = False
        if smb == 'X':
            scores[smb] += 1
        else:
            scores['O'] += 1 
        history.append(f'{smb} wins')
        update_score()

def can_win(a1, a2, a3, smb):
    count = 0
    spaces = []
    if a1['text'] == smb:
        count += 1
    elif a1['text'] == ' ':
        spaces.append(a1)
    if a2['text'] == smb:
        count += 1
    elif a2['text'] == ' ':
        spaces.append(a2)
    if a3['text'] == smb:
        count += 1
    elif a3['text'] == ' ':
        spaces.append(a3)
    if count == 2 and len(spaces) == 1:
        spaces[0]['text'] = 'O'
        return True
    else:
        return False

def computer_move():
    global cross_count
    if ai_level == "Difficile":
        for n in range(3):
            if can_win(field[n][0], field[n][1], field[n][2], 'O'):
                cross_count += 1
                check_win('O')
                return
            if can_win(field[0][n], field[1][n], field[2][n], 'O'):
                cross_count += 1
                check_win('O')
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'O'):
            cross_count += 1
            check_win('O')
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'O'):
            cross_count += 1
            check_win('O')
            return
        for n in range(3):
            if can_win(field[n][0], field[n][1], field[n][2], 'X'):
                return
            if can_win(field[0][n], field[1][n], field[2][n], 'X'):
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'X'):
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'X'):
            return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
ai_level = "Facile"

def change_ai_level():
    global ai_level
    if ai_level == "Facile":
        ai_level = "Difficile"
        ai_button.config(text="Niveau: Difficile")
    else:
        ai_level = "Facile"
        ai_button.config(text="Niveau: Facile")

ai_button = Button(root, text="Niveau: Facile" , relief=GROOVE, command=change_ai_level, background='black', fg='white')
ai_button.grid(row=5, column=0, columnspan=3, sticky='nsew')
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text = ' ', width = 4, height = 2,
                        font = ('Verdana', 30, 'bold'),
                        background='brown',
                        command = lambda row = row, col = col: click(row,col))
        button.grid(row = row, column = col, sticky = 'nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text = 'Restart', relief=GROOVE, command = new_game, bg ='black', fg='white')
new_button.grid(row = 3, column = 0, columnspan = 3, sticky = 'nsew')

root.mainloop() 
