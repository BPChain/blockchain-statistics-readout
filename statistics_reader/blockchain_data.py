import json
import os


class BlockchainData:
    def __init__(self, chain_name, host_id):
        self.hashrate = 0
        self.block_size = 0
        self.is_mining = 0
        self.cpu_usage = 0
        self.transactions = 0
        self.difficulty = 0
        self.time = 0
        self._data = {}
        self._data['chainName'] = chain_name
        self._data['hostId'] = host_id
        self._data['target'] = os.environ.get('TARGET_HOSTNAME', 'NO_HOST_SET')

    def to_dict(self):
        self._data['avgDifficulty'] = self.difficulty
        self._data['blockSize'] = self.block_size
        self._data['avgTransactions'] = self.transactions
        self._data['isMining'] = self.is_mining
        self._data['cpuUsage'] = self.cpu_usage
        self._data['hashrate'] = self.hashrate
        self._data['avgBlocktime'] = self.time
        return self._data
