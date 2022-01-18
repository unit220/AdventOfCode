# not my own code, follow link for source https://www.youtube.com/watch?v=zAjliaaIjIc

from __future__ import annotations
from typing import NamedTuple

# Read input from file
file = open('./input.txt', 'r')
lines = file.read()
file.close


class Board(NamedTuple):
    left: set[int]
    ints: list[int]

    # see if someone won
    @property
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.ints[i * 5 + j] in self.left:
                    break
            else:
                return True

            for j in range(5):
                if self.ints[i + 5 * j] in self.left:
                    break
            else:
                return True
        else:
            return False

    @classmethod
    def parse(cls, board: str) -> Board:
        ints = [int(s) for s in board.split()]
        left = set(ints)
        return cls(left, ints)


# parse ints/boards
first, *rest = lines.split('\n\n')
boards = [Board.parse(board) for board in rest]
ints = [int(s) for s in first.split(',')]


# call the nums and remove if hit
def get_number() -> int:
    for number in ints:
        for board in boards:
            board.left.discard(number)

        for board in boards:
            if board.has_won:
                return sum(board.left) * number

    raise AssertionError('unreachable')


print(get_number())

# Store called numbers
# calledNumbersStr = lines.split("\n")
# print(calledNumbersStr)
# calledNumbers = [calledNumbersStr.split(",")]
# print(calledNumbers)
