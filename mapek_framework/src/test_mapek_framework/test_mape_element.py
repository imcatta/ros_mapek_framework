import unittest
import mock
from mapek_framework.mape_element import _MapeElement,  MonitorElement, AnalyzeElement, PlanElement, ExecuteElement


class MyMapeElement(_MapeElement):
    def on_interaction_received(self, interaction, payload):
        pass


class MapeElementTestCase(unittest.TestCase):

    def test_mape_element_inheritance(self):
        self.assertTrue(issubclass(MonitorElement, _MapeElement))
        self.assertTrue(issubclass(AnalyzeElement, _MapeElement))
        self.assertTrue(issubclass(PlanElement, _MapeElement))
        self.assertTrue(issubclass(ExecuteElement, _MapeElement))

    def test_mape_element_send_interaction(self):
        interaction = 'interaction_name'
        payload = 'msg'
        m1 = mock.Mock()
        m2 = mock.MagicMock()
        m2.__getitem__.side_effect = lambda _: m1

        element = MyMapeElement(None, None)
        element.output_topics = m2
        element.send_interaction(interaction, payload)
        m2.__getitem__.assert_called_with(interaction)
        m1.publish.assert_called_with(payload)
