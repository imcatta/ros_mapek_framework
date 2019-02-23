import unittest
import mock
from mapek_framework.components import _MapeComponent, MonitorComponent, AnalyzeComponent, PlanComponent, ExecuteComponent
from mapek_framework import ManagedSystem, Interaction


class MyMapeComponent1(_MapeComponent):

    input_interactions = [Interaction('ii', None)] * 3
    output_interactions = [Interaction('o1', None)] * 4

    def on_interaction_received(self, interaction, payload):
        pass


class MyMapeComponent2(_MapeComponent):

    def on_interaction_received(self, interaction, payload):
        pass


class MyManagedSystem(ManagedSystem):
    pass


class ComponentsTestCase(unittest.TestCase):

    def test_mape_element_inheritance(self):
        self.assertTrue(issubclass(MonitorComponent, _MapeComponent))
        self.assertTrue(issubclass(AnalyzeComponent, _MapeComponent))
        self.assertTrue(issubclass(PlanComponent, _MapeComponent))
        self.assertTrue(issubclass(ExecuteComponent, _MapeComponent))

    @mock.patch('rospy.Publisher')
    @mock.patch('rospy.Subscriber')
    def test_mape_element_init(self, mock_subscriber, mock_publisher):
        knowledge = {}
        managed_system = MyManagedSystem()

        element = MyMapeComponent1(knowledge, managed_system)
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

        element = MyMapeComponent2(None, None)
        element.output_topics = m2
        element.send_interaction(interaction, payload)
        m2.__getitem__.assert_called_with(interaction)
        m1.publish.assert_called_with(payload)
