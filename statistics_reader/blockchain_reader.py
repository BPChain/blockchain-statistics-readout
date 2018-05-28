from statistics import mean

import psutil as psutil

from .blockchain_adapter import BlockchainAdapter
from .blockchain_data import BlockchainData


class BlockchainReader:
    def __init__(self, process_name: str, chain_name: str, adapter: BlockchainAdapter):
        self.process_name = process_name
        self.adapter = adapter
        self.data = BlockchainData(chain_name, adapter.host_id())

    def _cpu_usage(self):
        return sum([p.cpu_percent() for p in psutil.process_iter()
                    if self.process_name in p.name()]) / psutil.cpu_count()

    def _update_data(self):
        self.data.is_mining = self.adapter.is_mining()
        self.data.cpu_usage = self._cpu_usage()
        self.data.hashrate = self.adapter.hashrate()
        self._store_averages()

    def _store_averages(self):
        new_blocks, old_block = self.adapter.new_blocks_and_previous()
        if new_blocks:
            self.data.difficulty = mean(block.difficulty for block in new_blocks)
            self.data.block_size = mean(block.size for block in new_blocks)
            self.data.transactions = mean(len(block.transactions) for block in new_blocks)
        if old_block and new_blocks:
            if old_block.timestamp == 0:
                # The first block might have a timestamp 0 if it is the genesis block.
                # This would lead to a huge average
                old_block = new_blocks[0]
            self.data.time = (new_blocks[-1].timestamp - old_block.timestamp) / len(new_blocks)

    def read_json_data(self):
        self._update_data()
        return self.data.to_json()
