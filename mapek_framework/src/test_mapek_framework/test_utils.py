import unittest
import mock
from mapek_framework.utils import Ticker


class UtilsTestCase(unittest.TestCase):

    def test_ticker_init(self):
        node_name = 'foo_name'
        topic = 'foo_topic'
        rate = 42

        ticker_instance = Ticker(node_name, topic, rate)
        self.assertEqual(ticker_instance._node_name, node_name)
        self.assertEqual(ticker_instance._topic, topic)
        self.assertEqual(ticker_instance._rate, rate)

    def test_ticker_spin(self):
        node_name = 'foo_name'
        topic = 'foo_topic'
        rate = 42

        def is_shutdown():
            if not hasattr(is_shutdown, 'already_executed'):
                is_shutdown.already_executed = True
                return False

            return True

        ticker_instance = Ticker(node_name, topic, rate)

        with \
                mock.patch('rospy.is_shutdown', side_effect=is_shutdown) as mock_is_shutdown, \
                mock.patch('rospy.Rate') as mock_rate, \
                mock.patch('rospy.init_node') as mock_init_node, \
                mock.patch('rospy.Publisher'):

            ticker_instance.spin()
            self.assertEqual(mock_init_node.call_count, 1)
            mock_init_node.assert_called_with(node_name)
            self.assertEqual(mock_rate.call_count, 1)
            mock_rate.assert_called_with(rate)
            self.assertEqual(mock_is_shutdown.call_count, 2)
