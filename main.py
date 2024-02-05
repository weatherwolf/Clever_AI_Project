from game import *

# Create players
player1 = Player("Player 1", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 0)
player2 = Player("Player 2", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 1)
player3 = Player("Player 3", 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], 2)

players = [player1, player2, player3]

# Create a game with the players
game = Game(players)

# Start the game
game.start_game()

# Display the final scores
print("\nFinal Scores:")
for player in players:
    print(f"{player.name}: {player.score}")



# Initialize a round
# current_round = Round()

# yellow_board = YellowBoard()
# blue_board = BlueBoard()
# green_board = GreenBoard()
# orange_board = OrangeBoard()
# purple_board = PurpleBoard()

# boards = [yellow_board, blue_board, green_board, orange_board, purple_board]

# for i in range(5):
#     # Roll the dice
#     current_round.roll_dice()

#     # Display the initial state of the dice
#     print("Initial state of dice:")
#     if current_round.all_dice:
#         for dice in current_round.all_dice:
#             print(f"{dice.type} Dice: {dice.value}")

#         # Choose a random dice
#         chosen_dice = random.choice(current_round.all_dice)

#         # Display the chosen dice
#         print(f"\nChosen Dice: {chosen_dice.type} Dice, Value: {chosen_dice.value}")

#         # Choose dice and remove from the list
#         current_round.choose_dice(chosen_dice)

#         # Display the remaining dice
#         print("\nRemaining Dice:")
#         for dice in current_round.all_dice:
#             print(f"{dice.type} Dice: {dice.value}")

#         chosen_board = None
#         for board in boards:
#             if chosen_dice.type == board.get_color():
#                 chosen_board = board

#             elif chosen_dice.type == "White":
#                 chosen_board = random.choice

#         # Display the initial state of the Chosen Board
#         print(f"\nInitial state of the {chosen_board.get_color()} Board:")
#         for space in chosen_board.all_spaces:
#             if space.crossed:
#                 print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
#             else:
#                 print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")


#         # Cross a space on the Chosen Board
#         chosen_space = random.choice(chosen_board.available_spaces(chosen_dice.value))
#         print(f"space chosen with index {chosen_space.index} has value {chosen_space.dice_value}, The dice has value {chosen_dice.value}")

#         chosen_board.cross_space(chosen_space, chosen_dice.value)
#         if chosen_board.get_color() == "Blue":
#             chosen_board.cross_space(chosen_space, current_round.white_dice.value + current_round.blue_dice.value)
#         else:
#             chosen_board.cross_space(chosen_space, chosen_dice.value)
        

#         # Display the updated state of the Chosen Board
#         print(f"\nInitial state of the {chosen_board.get_color()} Board:")
#         for space in chosen_board.all_spaces:
#             if space.crossed:
#                 print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")
#             else:
#                 print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")

#         # Check and display bonuses on the Yellow Board
#         bonuses = chosen_board.check_bonus(chosen_space)
#         print("\nBonuses:")
#         print(bonuses)

#         # Get and display the score of the Yellow Board
#         score = chosen_board.get_score()
#         print(f"\nInitial state of the {chosen_board.get_color()} Board:")
    
#     else:
#         print("No dice left")

# scores = ScoreBoard(boards)
# print(f"The total score is: {scores.get_total_score()}")