import json

from statistics_reader.block import Block
from statistics_reader.blockchainreader import BlockchainReader
from .mock_adapter import MockAdapter


def setup_with(blocks):
    adapter = MockAdapter(hashrates=[3]*20, is_minings=[1]*20, new_blocks=blocks)
    return adapter, BlockchainReader('some_name', 'some_chain', adapter)


def test_avg_time_initial():
    blocks = [[Block(3, ['a', 'a', 'a'], 1101, 3), Block(3, ['a', 'a', 'a'], 1101, 3),
               Block(3, ['a', 'a', 'a'], 1101, 3)], []]
    adapter, reader = setup_with(blocks)
    reader._store_averages()
    assert 0 == reader.data.time
    adapter.next_epoch()
    reader._store_averages()
    assert 0 == reader.data.time


def test_avg_time_1():
    blocks = [[Block(3, ['a', 'a', 'a'], 5, 3)],
              [Block(3, ['a', 'a', 'a'], 10, 3), Block(3, ['a', 'a', 'a'], 20, 3),
               Block(3, ['a', 'a', 'a'], 33, 3)],
              []]
    adapter, reader = setup_with(blocks)
    reader._store_averages()
    assert 0 == reader.data.time
    adapter.next_epoch()
    reader._store_averages()
    assert (33 - 5) / 3 == reader.data.time
    adapter.next_epoch()
    reader._store_averages()
    assert (33 - 5) / 3 == reader.data.time


def test_avg_time_multiple_empty_epochs():
    blocks = [[Block(3, ['a', 'a', 'a'], 5, 3)],
              [Block(3, ['a', 'a', 'a'], 10, 3), Block(3, ['a', 'a', 'a'], 20, 3),
               Block(3, ['a', 'a', 'a'], 33, 3)],
              [], [], [],
              [Block(3, ['a', 'a', 'a'], 66, 3)], []]
    adapter, reader = setup_with(blocks)
    wanted_results = [0, (33 - 5) / 3, (33 - 5) / 3, (33 - 5) / 3, (33 - 5) / 3,
                      (66 - 33) / 1, (66 - 33) / 1]
    for result in wanted_results:
        reader._store_averages()
        assert result == reader.data.time
        adapter.next_epoch()


def test_avg_difficulty_multiple_empty_epochs():
    blocks = [[Block(3.6, ['a', 'a', 'a'], 5, 3)],
              [Block(3.9, ['a', 'a', 'a'], 10, 3), Block(3, ['a', 'a', 'a'], 20, 3),
               Block(6, ['a', 'a', 'a'], 33, 3)],
              [], [], [],
              [Block(1, ['a', 'a', 'a'], 66, 3)], []]
    adapter, reader = setup_with(blocks)
    wanted_results = [3.6, (3.9 + 3 + 6) / 3, (3.9 + 3 + 6) / 3, (3.9 + 3 + 6) / 3,
                      (3.9 + 3 + 6) / 3, 1]
    for result in wanted_results:
        reader._store_averages()
        assert result == reader.data.difficulty
        adapter.next_epoch()


def test_avg_difficulty_initial_empty_epochs():
    blocks = [[], [Block(3.6, ['a', 'a', 'a'], 5, 3)],
              [Block(3.9, ['a', 'a', 'a'], 10, 3), Block(3, ['a', 'a', 'a'], 20, 3),
               Block(6, ['a', 'a', 'a'], 33, 3)],
              [], [], [],
              [Block(1, ['a', 'a', 'a'], 66, 3)], []]
    adapter, reader = setup_with(blocks)
    wanted_results = [0, 3.6, (3.9 + 3 + 6) / 3, (3.9 + 3 + 6) / 3, (3.9 + 3 + 6) / 3,
                      (3.9 + 3 + 6) / 3, 1]
    for result in wanted_results:
        reader._store_averages()
        assert result == reader.data.difficulty
        adapter.next_epoch()


def test_avg_size_initial_empty_epochs():
    blocks = [[], [Block(3.6, ['a', 'a', 'a'], 5, 3)],
              [Block(3.9, ['a', 'a', 'a'], 10, 10), Block(3, ['a', 'a', 'a'], 20, 11),
               Block(6, ['a', 'a', 'a'], 33, 20)],
              [], [], [],
              [Block(1, ['a', 'a', 'a'], 66, 4)], []]
    adapter, reader = setup_with(blocks)
    wanted_results = [0, 3, (10 + 11 + 20) / 3, (10 + 11 + 20) / 3, (10 + 11 + 20) / 3,
                      (10 + 11 + 20) / 3, 4, 4]
    for result in wanted_results:
        reader._store_averages()
        assert result == reader.data.block_size
        adapter.next_epoch()


def test_avg_transactions_initial_empty_epochs():
    blocks = [[], [Block(3.6, ['a', 'a', 'a'], 5, 3)],
              [Block(3.9, ['a', 'a'], 10, 10), Block(3, ['a', 'a', 'a', 'a'], 20, 11),
               Block(6, ['a', 'a', 'a'], 33, 20)], [Block(1, ['a', 'a', 'a'], 66, 4)],
              [], [], [],
              [Block(1, [], 66, 4)], []]
    adapter, reader = setup_with(blocks)
    wanted_results = [0, 3, ((2 + 4 + 3) / 3), 3, 3, 3, 3, 0, 0]
    for result in wanted_results:
        reader._store_averages()
        assert result == reader.data.transactions
        adapter.next_epoch()


def test_json():
    blocks = [[], [Block(3.6, ['a', 'a', 'a'], 5, 3)],
              [Block(3.9, ['a', 'a'], 10, 10), Block(3, ['a', 'a', 'a', 'a'], 20, 11),
               Block(6, ['a', 'a', 'a'], 33, 20)], [Block(1, ['a', 'a', 'a'], 66, 4)],
              [], [], [],
              [Block(1, [], 66, 4)], []]
    adapter, reader = setup_with(blocks)
    data = reader.read_json_data()
    assert type(data) == str
    assert type(json.loads(data)) == dict
    adapter.next_epoch()
    data = reader.read_json_data()
    assert type(data) == str
    assert type(json.loads(data)) == dict
