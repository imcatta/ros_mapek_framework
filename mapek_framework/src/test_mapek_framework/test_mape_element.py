import unittest
import mock
from mapek_framework.mape_element import _MapeElement, MonitorElement, AnalyzeElement, PlanElement, ExecuteElement


class MapeElementTestCase(unittest.TestCase):

    def test_mape_element_inheritance(self):
        self.assertTrue(issubclass(MonitorElement, _MapeElement))
        self.assertTrue(issubclass(AnalyzeElement, _MapeElement))
        self.assertTrue(issubclass(PlanElement, _MapeElement))
        self.assertTrue(issubclass(ExecuteElement, _MapeElement))
