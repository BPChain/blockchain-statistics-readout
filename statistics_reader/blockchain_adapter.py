from typing import List, Tuple

from .block import Block


class BlockchainAdapter:

    def __init__(self, is_miner):
        self.is_miner = is_miner
        self.previous_block_number = 0

    def hashrate(self) -> int:
        raise NotImplementedError()

    def is_mining(self) -> int:
        raise NotImplementedError()

    def host_id(self):
        raise NotImplementedError()

    def new_blocks_and_previous(self) -> Tuple[List[Block], Block]:
        newest_block_number = self.fetch_newest_block_number()
        raw_blocks = [self.fetch_block_with(number)
                       for number in range(self.previous_block_number, newest_block_number + 1)]
        blocks = [self.make_block_from(raw_block) for raw_block in raw_blocks]
        old_block = blocks[0]
        new_blocks = blocks[1:] if len(blocks) > 1 else []
        return new_blocks, old_block

    def fetch_newest_block_number(self) -> int:
        raise NotImplementedError()

    def fetch_block_with(self, number: int):
        raise NotImplementedError()

    def make_block_from(self, raw_block) -> Block:
        raise NotImplementedError()
