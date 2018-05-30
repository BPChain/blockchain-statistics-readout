Travis: [![Build Status](https://travis-ci.org/BPChain/blockchain_statistics_readout.svg?branch=master)](https://travis-ci.org/BPChain/blockchain_statistics_readout)
Coveralls: [![Coverage Status](https://coveralls.io/repos/github/BPChain/blockchain_statistics_readout/badge.svg?branch=master)](https://coveralls.io/github/BPChain/blockchain_statistics_readout?branch=master)
CodeClimate: [![Maintainability](https://api.codeclimate.com/v1/badges/a9a3a37c323c0a0d945f/maintainability)](https://codeclimate.com/github/BPChain/blockchain_statistics_readout/maintainability)


### Statistics Reader
This is a Framework for reading statistics such as hashrate, average block-time, etc from a 
Blockchain. The framework is installed as a pip package. 

#### Usage
To use it one has to supply an Adapter object, a chain name and the process name of the blockchain
 process to the Sender class. `Sender(self, server_address: str, process_name: str, chain_name: 
 str, adapter: BlockchainAdapter, period=10)` Is the object needed to read and send data. For 
 more info read the documentation in [`sender`](statistics_reader/sender.py). This framework is 
 used by [private-multichain](https://github.com/BPChain/private-multichain), 
 [private-ethereum](https://github.com/BPChain/private-ethereum) and [private-ethereum](https://github.com/BPChain/private-xain). 
 
#### Install 
`pip3 install git+git://github.com/BPChain/blockchain_statistics_readout.git <br>
You can append a @1.1 to download that specific tag from this repo.

#### Architecture 
 [`Sender`](statistics_reader/sender.py) sends the data to the server. For this it uses a 
 [`Reader`](statistics_reader/blockchain_reader.py) object which reads the data with the help of 
 a [`BlockchainAdapter`](statistics_reader/blockchain_adapter.py) which has to be implemented by 
 each blockchain. The `Reader` also does some basic averaging of the data it collects. 
 
 #### Tests
 Tests for the reader are in the [`tests`](statistics_reader/tests) folder and test the 
 [`Reader`](statistics_reader/blockchain_reader.py). You can run them with `python3 -m pytest`