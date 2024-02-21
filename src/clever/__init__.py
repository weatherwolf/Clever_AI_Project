print("__init__.py")

from clever.game import Game
from clever.player import Player
from clever.board_specific import YellowBoard, BlueBoard, GreenBoard, OrangeBoard, PurpleBoard
# from ai import *

# test_ai = AI_Model()

# Create players
player1 = Player("Player 1", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 0)
player2 = Player("Player 2", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 1)
player3 = Player("Player 3", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 2)
player4 = Player("Player 4", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 3)

players = [player1, player2, player3]

# Create a game with the players
game = Game(players)

# Start the game
game.start_game()

# Display the final scores
print("\nFinal Scores:")
for player in players:
    print(f"{player.name}: {player.get_total_score()}")