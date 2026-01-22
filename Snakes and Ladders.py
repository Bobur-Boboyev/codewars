class SnakesLadders:
    def __init__(self):
        self.players = [0, 0]
        self.current = 0
        self.game_over = False
        self.board = {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44,
            51: 67, 71: 91, 78: 98, 87: 94, 16: 6, 46: 25, 49: 11,
            62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80
        }

    def play(self, die1: int, die2: int) -> str:
        if self.game_over:
            return "Game over!"

        player = self.current
        pos = self.players[player] + die1 + die2

        if pos > 100:
            pos = 100 - (pos - 100)

        pos = self.board.get(pos, pos)

        self.players[player] = pos

        if pos == 100:
            self.game_over = True
            return f"Player {player + 1} Wins!"

        if die1 != die2:
            self.current = 1 - self.current

        return f"Player {player + 1} is on square {pos}"