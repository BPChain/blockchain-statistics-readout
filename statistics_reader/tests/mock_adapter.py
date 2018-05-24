from typing import List
from itertools import chain

from statistics_reader.block import Block
from statistics_reader.blockchain_adapter import BlockchainAdapter


class MockAdapter(BlockchainAdapter):
    def __init__(self, hashrates: List[int] = (), is_minings: List[int] = (),
                 new_blocks: List[List[Block]] = ()):
        self.hashrates = hashrates
        self.is_minings = is_minings
        self.blocks = new_blocks
        self.old_block = None
        self.epoch = 0

    def host_id(self):
        return 'some_id'

    def hashrate(self) -> int:
        return self.hashrates[self.epoch]

    def is_mining(self) -> int:
        return self.is_minings[self.epoch]

    def new_blocks_and_previous(self):
        result = self.blocks[self.epoch], self.old_block
        if len(self.blocks) > self.epoch and self.blocks[self.epoch]:
            self.old_block = self.blocks[self.epoch][-1]
        return result

    def next_epoch(self):
        self.epoch += 1
