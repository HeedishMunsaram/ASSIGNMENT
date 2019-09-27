player1 = input("Player 1, please enter your choice either rock or paper or scissors: ")
player2 = input("Player 2, please enter your choice either rock or paper or scissors: ")

if (player1 == 'rock' and player2 == 'scissors'):
    print("Congratulation player 1 wins.")

elif (player1 == 'rock' and player2 == 'rock'):
    print("It's a tie")

elif (player1 == 'scissors' and player2 == 'paper'):
    print("Congratulation player 1 wins.")

elif (player2 == 'scissors' and player2 == 'scissors'):
    print("It's a tie")

elif (player1 == 'paper' and player2 == 'paper'):
    print("It's a tie")

elif (player1 == 'paper' and player2 == 'scissors'):
    print("Congratulation player 2 wins.")

elif (player1 == 'rock'and player2 == 'paper'):
    print("Congratulation player 2 wins.")

elif (player1 == 'paper' and player2 == 'rock'):
    print("Congratulation player 2 wins.")

elif (player1 == 'scissors' and player2 == 'rock'):
    print("Congratulation player 2 wins.")
