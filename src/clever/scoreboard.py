from clever.board import Board

class ScoreBoard:
    def __init__(self, boards: list[Board]) -> None:

        self.boards = boards


    def get_total_score(self) -> int:

        total_score = 0
        for board in self.boards:
            print(f"The score for the {board.color} board is: {board.get_score()}")
            total_score += board.get_score()
        return total_score
