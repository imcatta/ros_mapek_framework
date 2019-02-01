import unittest
import mock
from mapek_framework.mape_element import _MapeElement,  MonitorElement, AnalyzeElement, PlanElement, ExecuteElement
from mapek_framework import ManagedSystem, Interaction


class MyMapeElement1(_MapeElement):

    input_interactions = [Interaction('ii', None)] * 3
    output_interactions = [Interaction('o1', None)] * 4

    def on_interaction_received(self, interaction, payload):
        pass


class MyMapeElement2(_MapeElement):

    def on_interaction_received(self, interaction, payload):
        pass


class MyManagedSystem(ManagedSystem):
    pass


class MapeElementTestCase(unittest.TestCase):

    def test_mape_element_inheritance(self):
        self.assertTrue(issubclass(MonitorElement, _MapeElement))
        self.assertTrue(issubclass(AnalyzeElement, _MapeElement))
        self.assertTrue(issubclass(PlanElement, _MapeElement))
        self.assertTrue(issubclass(ExecuteElement, _MapeElement))

    @mock.patch('rospy.Publisher')
    @mock.patch('rospy.Subscriber')
    def test_mape_element_init(self, mock_subscriber, mock_publisher):
        knowledge = {}
        managed_system = MyManagedSystem()

        element = MyMapeElement1(knowledge, managed_system)
        self.assertEqual(element.knowledge, knowledge)
        self.assertEqual(element.managed_system, managed_system)
        self.assertEqual(mock_subscriber.call_count, 3)
        self.assertEqual(mock_publisher.call_count, 4)

    def test_mape_element_send_interaction(self):
        interaction = 'interaction_name'
        payload = 'msg'
        m1 = mock.Mock()
        m2 = mock.MagicMock()
        m2.__getitem__.side_effect = lambda _: m1

        element = MyMapeElement2(None, None)
        element.output_topics = m2
        element.send_interaction(interaction, payload)
        m2.__getitem__.assert_called_with(interaction)
        m1.publish.assert_called_with(payload)
