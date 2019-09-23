# I, Sean Flannigan, student number 000270501, certify that all code
# submitted is my own work; that I have not copied it from any
# other source.  I also certify that I have not allowed my work to be
# copied by others.


# random library used for rock paper scissors game and turn order selection
import random

# module for rock paper scissors game, called after player chooses a move
def rockPaperGame(playerName):
    noTieFlag = False
    validInputFlag = False
    
    # validation loop for player input
    while validInputFlag is False:
        playerChoice = input("{} please enter one of the following: Rock, Paper, Scissors, Lizard, Spock: ".format(playerName))
        if playerChoice.lower() == "rock" or playerChoice.lower() == "paper" \
           or playerChoice.lower() == "scissors" or playerChoice.lower() == "lizard" \
           or playerChoice.lower() == "spock":
            validInputFlag = True
        else:
            print("Sorry, that isn't a valid input.")
            validInputFlag = False

    # validation loop to ensure no ties occur
    while noTieFlag is False:
        computerChoice = random.randrange(0, 5)
        if computerChoice == 0:
            computerRPS = "rock"
        elif computerChoice == 1:
            computerRPS = "paper"
        elif computerChoice == 2:
            computerRPS = "scissors"
        elif computerChoice == 3:
            computerRPS = "lizard"
        elif computerChoice == 4:
            computerRPS = "spock"
            
        if computerRPS == playerChoice.lower():
            noTieFlag = False
        else:
            noTieFlag = True
        
    # 5 cases for playerChoice with 4 nested cases to declare a winner
    if playerChoice.lower() == "rock":
        if computerRPS == "scissors":
            print("Computer chose scissors. Rock crushes scissors! {} wins!".format(playerName))
            return True
        elif computerRPS == "lizard":
            print("Computer chose lizard. Rock crushes lizard! {} wins!".format(playerName))
            return True
        elif computerRPS == "spock":
            print("Computer chose Spock. Spock vaporizes rock! Computer wins!")
            return False
        elif computerRPS == "paper":
            print("Computer chose paper. Paper covers rock! Computer wins!")
            return False
    elif playerChoice.lower() == "scissors":
        if computerRPS == "paper":
            print("Computer chose paper. Scissors cuts paper! {} wins!".format(playerName))
            return True
        elif computerRPS == "lizard":
            print("Computer chose lizard. Scissors decapitates lizard! {} wins!".format(playerName))
            return True
        elif computerRPS == "rock":
            print("Computer chose rock. Rock crushes scissors! Computer wins!")
            return False
        elif computerRPS == "spock":
            print("Computer chose Spock. Spock smashes scissors! Computer wins!")
            return False
    elif playerChoice.lower() == "spock":
        if computerRPS == "scissors":
            print("Computer chose scissors. Spock smashes scissors! {} wins!".format(playerName))
            return True
        elif computerRPS == "rock":
            print("Computer chose rock. Spock vaporizes rock! {} wins!".format(playerName))
            return True
        elif computerRPS == "lizard":
            print("Computer chose lizard. Lizard poisons Spock! Computer wins!")
            return False
        elif computerRPS == "paper":
            print("Computer chose paper. Paper disproves Spock! Computer wins!")
            return False
    elif playerChoice.lower() == "lizard":
        if computerRPS == "spock":
            print("Computer chose Spock. Lizard poisons Spock! {} wins!".format(playerName))
            return True
        elif computerRPS == "paper":
            print("Computer chose paper. Lizard eats paper! {} wins!".format(playerName))
            return True
        elif computerRPS == "rock":
            print("Computer chose rock. Rock crushes lizard! Computer wins!")
            return False
        elif computerRPS == "scissors":
            print("Computer chose scissors. Scissors decapitates lizard! Computer wins!")
            return False
    elif playerChoice.lower() == "paper":
        if computerRPS == "rock":
            print("Computer chose rock. Paper covers rock! {} wins!".format(playerName))
            return True
        elif computerRPS == "spock":
            print("Computer chose Spock. Paper disproves Spock! {} wins!".format(playerName))
            return True
        elif computerRPS == "scissors":
            print("Computer chose scissors. Scissors cuts paper! Computer wins!")
            return False
        elif computerRPS == "lizard":
            print("Computer chose lizard. Lizard eats paper! Computer wins!")
            return False

# validation check when a rock paper scissors loss occurs but
# a swap of tiles would cause a game win for the loser's opponent
def rockPaperGameLossCheck():
    if a == b and a == c:
        return True   
    elif d == e and d == f:
        return True
    elif g == h and g == i:
        return True
    elif a == d and a == g:
        return True
    elif b == e and b == h:
        return True
    elif c == f and c == i:
        return True
    elif a == e and a == i:
        return True
    elif c == e and c == g:
        return True
    else:
        return False
               

# board storage, called and adjusted throughout main game
def ticTacToeBoard():
    print("                    ")
    print("            |   |   ")
    print("          {} | {} | {} ".format(a, b, c))
    print("            |   |   ")
    print("         --- --- ---")
    print("            |   |   ")
    print("          {} | {} | {} ".format(d, e, f))
    print("            |   |   ")
    print("         --- --- ---")
    print("            |   |   ")
    print("          {} | {} | {} ".format(g, h, i))
    print("            |   |   ")


# validation check to adjust the play again flag
def newGameCheck():
    gameCheck = input("\n\nEnter y or yes if you'd like to play again, or anything else to exit: ")
    if gameCheck.lower() == "y" or gameCheck.lower() == "yes":
        return True
    else:
        return False

# flag controlling main game code
playAgainFlag = True

# main code loop
while playAgainFlag is True:

    # initialization of board values to display available positions
    a = "1"
    b = "2"
    c = "3"
    d = "4"
    e = "5"
    f = "6"
    g = "7"
    h = "8"
    i = "9"

    # initial values for further use
    print("\nWelcome to CompSci Squares!\n\n")
    player1Name = input("Please enter the first player's name: ")
    player2Name = input("Please enter the second player's name: ")
    firstPlayer = ""
    secondPlayer = ""
    firstPlayerLetter = "X"
    secondPlayerLetter = "O"
    winFlag = False
    tieFlag = False
    moveChoice = False
    num = ""

    # block to determine the first player and X - O assignment
    letterChoice = random.randrange(0, 2)
    if letterChoice == 0:
        firstPlayer = player1Name
        firstPlayerLetter = "X"
        secondPlayer = player2Name
        secondPlayerLetter = "O"
        print("\n{} is X's and will play first!\n".format(firstPlayer))
    elif letterChoice == 1:
        firstPlayer = player2Name
        firstPlayerLetter = "X"
        secondPlayer = player1Name
        secondPlayerLetter = "O"
        print("\n{} is X's and will play first!\n".format(firstPlayer))

    # main tic tac toe loop, using initial flags above
    while tieFlag is False and winFlag is False:
        # each round begins with board display
        ticTacToeBoard()

        # first set of if elifs determine if a win condition exists before
        # new play occurs
        if tieFlag is True or winFlag is True:
            print("\n")
        elif a == b and a == c:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif d == e and d == f:
            winFlag = True
            print("\n{}'s win the game!".format(d))
        elif g == h and g == i:
            winFlag = True
            print("\n{}'s win the game!".format(g))
        elif a == d and a == g:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif b == e and b == h:
            winFlag = True
            print("\n{}'s win the game!".format(b))
        elif c == f and c == i:
            winFlag = True
            print("\n{}'s win the game!".format(c))
        elif a == e and a == i:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif c == e and c == g:
            winFlag = True
            print("\n{}'s win the game!".format(c))
        # next elif determines if a tie exists but not a win before
        # new play occurs
        elif (a == "X" or a == "O") and (b == "X" or b == "O") \
           and (c == "X" or c == "O") and (d == "X" or d == "O") \
           and (e == "X" or e == "O") and (f == "X" or f == "O") \
           and (g == "X" or g == "O") and (h == "X" or h == "O") \
           and (i == "X" or i == "O"):
            tieFlag = True
            print("\nTie Game!")
        # else result to resume play and place a new X or O
        else:
            # initial move flag and loop to determine spot selection
            # result and ensure spot chosen is clear. each (el)if-nested-
            # if-else-nested-if-else corresponds to a spot on the board
            # and the actions required to determine if an X or O is placed.
            # these are also where the rock paper scissors module is called.
            # final else controls the False flag repeat of the loop on bad
            # spot selection. this block is for the first player
            moveChoice = False
            while moveChoice is False:
                print("\nIt is {}'s turn to place an {}.".format(firstPlayer, firstPlayerLetter))
                num = input("Select an open place on the board (1-9): ")
                if num == a:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        a = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        a = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            a = "1"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == b:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        b = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        b = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            b = "2"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == c:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        c = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        c = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            c = "3"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == d:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        d = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        d = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            d = "4"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == e:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        e = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        e = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            e = "5"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == f:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        f = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        f = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            f = "6"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == g:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        g = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        g = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            g = "7"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == h:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        h = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        h = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            h = "8"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                elif num == i:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(firstPlayer)
                    if rpsFlag is True:
                        i = firstPlayerLetter
                        print("\n{} takes the spot!".format(firstPlayer))
                    else:
                        i = secondPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(secondPlayer))
                            i = "9"
                        else:
                            print("\n{} takes the spot instead!".format(secondPlayer))
                else:
                    print("\nSorry, that is not a valid entry or that space is not free to select!")
                    moveChoice = False

            # each round begins with board display
            ticTacToeBoard()
        # first set of if elifs determine if a win condition exists before
        # new play occurs
        if tieFlag is True or winFlag is True:
            print("\n")
        elif a == b and a == c:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif d == e and d == f:
            winFlag = True
            print("\n{}'s win the game!".format(d))
        elif g == h and g == i:
            winFlag = True
            print("\n{}'s win the game!".format(g))
        elif a == d and a == g:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif b == e and b == h:
            winFlag = True
            print("\n{}'s win the game!".format(b))
        elif c == f and c == i:
            winFlag = True
            print("\n{}'s win the game!".format(c))
        elif a == e and a == i:
            winFlag = True
            print("\n{}'s win the game!".format(a))
        elif c == e and c == g:
            winFlag = True
            print("\n{}'s win the game!".format(c))
        # next elif determines if a tie exists but not a win before
        # new play occurs
        elif (a == "X" or a == "O") and (b == "X" or b == "O") \
           and (c == "X" or c == "O") and (d == "X" or d == "O") \
           and (e == "X" or e == "O") and (f == "X" or f == "O") \
           and (g == "X" or g == "O") and (h == "X" or h == "O") \
           and (i == "X" or i == "O"):
            tieFlag = True
            print("\nTie Game!")
        # else result to resume play and place a new X or O
        else:
            # initial move flag and loop to determine spot selection
            # result and ensure spot chosen is clear. each (el)if-nested-
            # if-else-nested-if-else corresponds to a spot on the board
            # and the actions required to determine if an X or O is placed.
            # these are also where the rock paper scissors module is called.
            # final else controls the False flag repeat of the loop on bad
            # spot selection. this block is for the second player.
            moveChoice = False
            while moveChoice is False:
                print("\nIt is {}'s turn to place an {}.".format(secondPlayer, secondPlayerLetter))
                num = input("Select an open place on the board (1-9): ")
                if num == a:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        a = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        a = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            a = "1"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == b:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        b = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        b = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            b = "2"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == c:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        c = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        c = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            c = "3"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == d:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        d = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        d = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            d = "4"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == e:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        e = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        e = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            e = "5"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == f:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        f = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        f = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            f = "6"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == g:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        g = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        g = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            g = "7"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == h:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        h = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        h = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            h = "8"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                elif num == i:
                    moveChoice = True
                    print("\nYou must win a game of Rock Paper Scissors Lizard Spock to win the spot!\n")
                    rpsFlag = rockPaperGame(secondPlayer)
                    if rpsFlag is True:
                        i = secondPlayerLetter
                        print("\n{} takes the spot!".format(secondPlayer))
                    else:
                        i = firstPlayerLetter
                        if rockPaperGameLossCheck() == True:
                            print("\n{} would win the game if they were given this spot, so it remains free!".format(firstPlayer))
                            i = "9"
                        else:
                            print("\n{} takes the spot instead!".format(firstPlayer))
                else:
                    print("\nSorry, that is not a valid entry or that space is not free to select!")
                    moveChoice = False

    # once main tic tac toe game loop is broken, new game check module is called to determine
    # true or false status of the playAgainFlag, which controls the overall code loop and
    # causes a full board reset or final code exit
    playAgainFlag = newGameCheck()

    # final pause before reset or exit
    pause = input("Press any key to continue")
    
