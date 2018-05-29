from time import sleep

import requests as http_client

from .blockchain_reader import BlockchainReader
from .logger import logger_for

LOGGER = logger_for(__name__)


class Sender:
    def __init__(self, server_address, period, reader: BlockchainReader):
        """
        :param server_address: the address of the server e.g. http://myserver.com/route
        :param period: wait period between data sends in seconds
        :param reader: a reader initialized with a blockchain adapter
        """
        self.reader = reader
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
                LOGGER.warning("Exception occurred during sending: '%s'", exception)
