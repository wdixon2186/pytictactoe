num = 0
player1 = input("Do you want to be X's or O's? please enter an X or O")
player2 = ''
if player1.lower() == 'x':
    player1 = 'X'
    player2 = 'O'
elif player1.lower() == 'o':
    player1 = 'O'
    player2 = 'X'
else:
    print("I'm sorry, that's not valid.")

print("Player 1 is " + player1 + ". Player 2 is " + player2)

print("Let's set up a board.")
game = ["","","","","","","","",""]

def create_board(board):
    print(board[6] + "|" + board[7] + "|" + board[8])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[0] + "|" + board[1] + "|" + board[2])

create_board(game)

def check_winner1():
    if game[0] == player1 and game[1] == player1 and game[2] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[3] == player1 and game[4] == player1 and game[5] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[6] == player1 and game[7] == player1 and game[8] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[6] == player1 and game[3] == player1 and game[0] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[7] == player1 and game[4] == player1 and game[1] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[8] == player1 and game[5] == player1 and game[2] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[6] == player1 and game[4] == player1 and game[2] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a
    elif game[8] == player1 and game[4] == player1 and game[0] == player1:
        print(player1 + "'s Wins thank you for playing!")
        return a

def check_winner2():
    if game[0] == player2 and game[1] == player2 and game[2] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[3] == player2 and game[4] == player2 and game[5] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[6] == player2 and game[7] == player2 and game[8] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[6] == player2 and game[3] == player2 and game[0] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[7] == player2 and game[4] == player2 and game[1] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[8] == player2 and game[5] == player2 and game[2] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[6] == player2 and game[4] == player2 and game[2] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a
    elif game[8] == player2 and game[4] == player2 and game[0] == player2:
        print(player2 + "'s Wins. Thank you for playing!")
        return a


while num < 9:
    choice1 = int(input("player1 where would you like to move first?"))
    answer = choice1 - 1
    game[answer] = player1
    create_board(game)
    check_winner1()
    num += 1

    if num >= 9:
        break

    choice2 = int(input("player2 where would you like to move first?"))
    answer = choice2 - 1
    game[answer] = player2
    create_board(game)
    check_winner2()
    num += 1

print("You tied. :/ ")