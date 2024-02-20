from game import *
from ai import *

test_ai = AI_Model()

# Create players
player1 = Player("Player 1", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 0, test_ai)
player2 = Player("Player 2", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 1, test_ai)
player3 = Player("Player 3", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 2, test_ai)
player4 = Player("Player 4", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 3, test_ai)

players = [player1, player2, player3]

# Create a game with the players
game = Game(players)

# Start the game
game.start_game()

# Display the final scores
print("\nFinal Scores:")
for player in players:
    print(f"{player.name}: {player.get_total_score()}")