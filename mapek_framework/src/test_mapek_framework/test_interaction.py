import unittest
from std_msgs.msg import Empty
from mapek_framework import Interaction


class InteractionTestCase(unittest.TestCase):

    def test_interaxction_fields(self):
        name = 'foo'
        data_class = Empty

        interaction_instance = Interaction(name, data_class)
        self.assertEqual(interaction_instance.name, name)
        self.assertEqual(interaction_instance.data_class, data_class)
