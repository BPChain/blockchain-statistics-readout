from typing import List


class Block:
    def __init__(self, difficulty: float, transactions: List, timestamp: int, size: int):
        self.difficulty = difficulty
        self.transactions = transactions
        self.timestamp = timestamp
        self.size = size
