import unittest
from mapek_framework import Ticker


class TickerTestCase(unittest.TestCase):

    def test_ticker_init(self):
        node_name = 'foo_name'
        topic = 'foo_topic'
        rate = 42

        ticker_instance = Ticker(node_name, topic, rate)
        self.assertEqual(ticker_instance._node_name, node_name)
        self.assertEqual(ticker_instance._topic, topic)
        self.assertEqual(ticker_instance._rate, rate)
