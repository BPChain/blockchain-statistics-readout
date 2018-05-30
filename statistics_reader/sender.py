from time import sleep

import requests as http_client

from .blockchain_reader import BlockchainAdapter, BlockchainReader
from .logger import logger_for

LOGGER = logger_for(__name__)


class Sender:
    def __init__(self, server_address: str, process_name: str, chain_name: str,
                 adapter: BlockchainAdapter, period=10):
        """
        I continuously send blockchain statistics to a server
        :param server_address: Where to send the data such as "http://myserver.com/route"
        :param process_name: name of the blockchain process
        :param chain_name: Name of blockchain
        :param adapter: An adapter for the blockchain, subclassing BlockchainAdapter
        :param period: How often in seconds data is send
        """
        self.reader = BlockchainReader(process_name, chain_name, adapter)
        self.send_data_every(period, server_address)

    def send_data_every(self, period, server_address):
        while True:
            sleep(period)
            try:
                json_data = self.reader.read_dict_data()
                LOGGER.info(json_data)
                response = http_client.post(server_address, json=json_data)
                LOGGER.info('Sent data, received %s from server', response.status_code)
            except Exception as exception:
                LOGGER.exception("Exception occurred during sending: '%s'", exception)
