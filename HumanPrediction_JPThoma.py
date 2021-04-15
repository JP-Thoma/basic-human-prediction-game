# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:22:57 2021
@author: Jan P. Thoma
"""
#####The Human Prediction Game######
def linear_congruence(xi):
    """Function to calculate linear congruences value and computer bet"""
    a = 22695477
    b = 1
    m = 2**32
    xi_plus1 = (a * xi + b) % m
    if xi_plus1 <= 2**31:
        cpu_move = 0
    else:
        cpu_move = 1
    return cpu_move, xi_plus1 

def input_difficulty(msg=''):
    """This function ensures execution of code even if player chooses invalid difficulty"""
    while(True):
        try: 
            difficulty=int(input(msg))
            if difficulty == 1 or difficulty == 2:
                break # was able to convert to 1 or 2 integers
            else: 
                print("Difficulty level must be 1 or 2")
        except:
            print("Difficulty level must be 1 or 2")
            pass # it will repeat the loop
    return (difficulty)

def input_moves(msg=''):
    """This function ensures execution of code even if player chooses invalid number of moves"""
    while(True):
        try: 
            moves=int(input(msg))
            if moves > 0:
                break # was able to convert to integers larger than 0
            else:
                print("Moves must be an integer larger than 0")
        except:
            print("Moves must be an integer larger than 0")
            pass # it will repeat the loop
    return (moves)

def input_player_choice(msg=''):
    """This function ensures that human player choses only between 0 and 1 during the game"""
    while(True):
        try: 
            player_move=int(input(msg))
            if player_move == 0 or player_move == 1:
                break # was able to convert to 0 or 1 integers
            else: 
                print("Fairplay please ;) You must choose either 0 or 1.")
        except:
            print("Fairplay please ;) You must choose either 0 or 1.")
            pass # it will repeat the loop
    return (player_move)

def cpu_prediction(player_move,throw10, throw00, throw11, throw01):
    """According to instructions CPU has four choices depending on the player's choice and count of sequential moves otherwise CPU will choose randomly"""
    if player_move == 0 and throw10 > throw00:
        cpu_move = 1
    elif player_move == 0 and throw10 < throw00:
        cpu_move = 0
    elif player_move == 1 and throw11 > throw01:
        cpu_move = 1
    elif player_move == 1 and throw11 < throw01:
        cpu_move = 0
    else:
        cpu_move,xi2 = linear_congruence(xi)
    return cpu_move

def final_winner(PS,MS):
    """This function and announces the final winner of one complete game after n rounds"""
    if PS > MS:
        print("You win against the machine of doom! Well done " + player + ". Final result: You: %d Computer: %d" % (PS,MS))
    elif MS > PS:
        print("Unlucky, the machine defeated you. You have to train harder " + player + ". Final result: You: %d Computer: %d" % (PS,MS))
    else:
        print("A draw! This happens when an immovable object meets an unstoppable force. Now try to win " + player + ". Final result: You: %d Computer: %d" % (PS,MS))

def victory_count(PS,MS,PTW,CTW):
    """This function counts the final results of victories"""
    if PS > MS:
        PTW = PTW + 1
    elif MS > PS:
        CTW = CTW + 1
    else:
        pass
    return(PTW,CTW)

print("Welcome to Human Behavior Prediction by Jan P. Thoma")
player = input("What is your name? ")
print("Hello " + player + "! Get ready to defeat the machine.")

xi = 1234 #seed
PTW = 0 #Player total wins
CTW = 0 #Computer total wins

#Wrapping the game into a while loop for restart option
while True:
    difficulty = input_difficulty("Please choose the type of game (1: Easy, 2: Difficult): ")
    moves = input_moves("Please enter number of moves you would like to play: ")
    
    MS = 0 #Initialised CPU Victories
    PS = 0 #Initialised Human Victories
    throw00 = 0 #player choice count of 0 following a 0  
    throw01 = 0 #player choice count of 0 following a 1 
    throw10 = 0 #player choice count of 1 following a 0 
    throw11 = 0 #player choice count of 1 following a 1 

    #The Game
    if difficulty == 1: #easy mode
        for turn in range(moves):
            player_move = input_player_choice("Choose your number %s (0 or 1): " % (turn+1))
            computer_move, xi = linear_congruence(xi)
            if player_move == computer_move:
                MS = MS + 1 #calculate machine score
                print(player + " = %d machine = %d - Machine wins!" % (player_move,computer_move)) # machine won announcemnet with move results
                print("You: %d Computer: %d" % (PS,MS)) #total machine score
            else: 
                PS = PS + 1 #calculate player score 
                print(player + " = %d machine = %d - player wins!" % (player_move,computer_move)) #player won announcement with move results
                print("You: %d Computer: %d" % (PS,MS)) #total player score
            
            print(player + "*"*PS)
            print("COMPUTER: " + "*"*MS)
        final_winner(PS,MS)
        PTW,CTW = victory_count(PS,MS,PTW,CTW)
    
    if difficulty == 2:
        previous = None
        for turn in range(moves):
            computer_move = cpu_prediction(previous,throw10, throw00, throw11, throw01)
            player_move = input_player_choice("Choose your number %s (0 or 1): " % (turn+1))
            current = player_move
            
            if previous == 0 and current == 0:
                throw00 = throw00 + 1
            elif previous == 0 and current == 1:
                throw10 = throw10 + 1
            elif previous == 1 and current == 0:
                throw01 = throw01 + 1
            elif previous == 1 and current == 1:
                throw11 = throw11 + 1
            else:
                pass
            previous = current
            
            if player_move == computer_move:
                MS = MS + 1 #calculate machine score
                print(player + " = %d machine = %d - Machine wins!" % (player_move,computer_move)) # machine won announcemnet with move results
                print("You: %d Computer: %d" % (PS,MS)) #total machine score
            else: 
                PS = PS + 1 #calculate player score 
                print(player + " = %d machine = %d - player wins!" % (player_move,computer_move)) #player won announcement with move results
                print("You: %d Computer: %d" % (PS,MS)) #total player score
            
            print(player + "*"*PS)
            print("COMPUTER: " + "*"*MS)
        final_winner(PS,MS)
        PTW,CTW = victory_count(PS,MS,PTW,CTW)

    #restarting the game
    restart = input("Do you want to restart the game? Y/N ")
    if restart == "Y":
        continue
    else:
        print("Thanks for playing! Have a great day " + player + " :) \nYour Total Wins: %d  Computer Total Wins: %d" % (PTW,CTW)) 
        break           


            
            
