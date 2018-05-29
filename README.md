Travis: [![Build Status](https://travis-ci.org/BPChain/blockchain_statistics_readout.svg?branch=master)](https://travis-ci.org/BPChain/blockchain_statistics_readout)
Coveralls: [![Coverage Status](https://coveralls.io/repos/github/BPChain/blockchain_statistics_readout/badge.svg?branch=master)](https://coveralls.io/github/BPChain/blockchain_statistics_readout?branch=master)
CodeClimate: [![Maintainability](https://api.codeclimate.com/v1/badges/a9a3a37c323c0a0d945f/maintainability)](https://codeclimate.com/github/BPChain/blockchain_statistics_readout/maintainability)

This is a Framework for reading statistics such as hashrate, average block time, etc from a 
Blockchain.

To use it on has to supply an Adapter object, a chain name and the process name of the blockchian
 process to the Reader class. Pass that class and the server Address to the Sender class.