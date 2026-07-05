player1 = input("\nPlayer 1 (rock/paper/scissors): ").lower()
player2 = input("Player 2 (rock/paper/scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")