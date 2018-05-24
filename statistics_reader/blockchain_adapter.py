from typing import List, Tuple

from .block import Block


class BlockchainAdapter:

    def __init__(self, is_miner):
        self.is_miner = is_miner

    def hashrate(self) -> int:
        raise NotImplementedError()

    def is_mining(self) -> int:
        raise NotImplementedError()

    def host_id(self):
        raise NotImplementedError()

    def new_blocks_and_previous(self) -> Tuple[List[Block], Block]:
        raise NotImplementedError()
