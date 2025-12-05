def Rock_Paper_Scissors(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

print(Rock_Paper_Scissors('rock', 'scissors'))  
print(Rock_Paper_Scissors('scissors', 'rock'))   
print(Rock_Paper_Scissors('scissors', 'paper'))  
print(Rock_Paper_Scissors('paper', 'paper'))     