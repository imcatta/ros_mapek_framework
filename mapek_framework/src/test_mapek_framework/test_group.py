import unittest
import mock
from mapek_framework import Group


class GroupTestCase(unittest.TestCase):

    @mock.patch('rospy.spin')
    @mock.patch('rospy.init_node')
    def test_group_spin(self, mock_init_node, mock_spin):
        node_name = 'test_node'

        mock_monitor_element = mock.Mock()
        mock_analyze_element = mock.Mock()
        mock_plan_element = mock.Mock()
        mock_execute_element = mock.Mock()

        knowledge_instance = {}
        managed_system_instance = None

        class MyGroup(Group):
            elements = [
                mock_monitor_element,
                mock_analyze_element,
                mock_plan_element,
                mock_execute_element
            ]
            knowledge = knowledge_instance
            managed_system = managed_system_instance

        my_group_instance = MyGroup(node_name)
        self.assertEqual(mock_init_node.call_count, 1)
        self.assertEqual(mock_spin.call_count, 0)
        mock_monitor_element.assert_called_with(knowledge_instance, managed_system_instance)
        mock_analyze_element.assert_called_with(knowledge_instance, managed_system_instance)
        mock_plan_element.assert_called_with(knowledge_instance, managed_system_instance)
        mock_execute_element.assert_called_with(knowledge_instance, managed_system_instance)

        my_group_instance.spin()
        self.assertEqual(mock_init_node.call_count, 1)
        self.assertEqual(mock_spin.call_count, 1)
