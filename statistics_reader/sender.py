from time import sleep

from websocket import create_connection

from .blockchainreader import BlockchainReader
from ..logger import logger_for

LOGGER = logger_for(__name__)


class Sender:
    def __init__(self, server_address, period, reader: BlockchainReader):
        self.reader = reader
        self.send_data_every(period, server_address)

    def send_data_every(self, period, server_address):
        while True:
            sleep(period)
            try:
                web_socket = create_connection(server_address, 10)
                data = self.reader.read_json_data()
                LOGGER.info(data)
                web_socket.send()
                LOGGER.info("Sent data ")
                result = web_socket.recv()
                LOGGER.info("Received '%s'", result)
                web_socket.close()
            except Exception as exception:
                LOGGER.warning("Exception occurred during sending: '%s'", exception)
