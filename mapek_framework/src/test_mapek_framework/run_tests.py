#!/usr/bin/env python
import unittest
import rosunit
from .test_group import GroupTestCase
from .test_interaction import InteractionTestCase
from .test_managed_system import ManagedSystemTestCase
from .test_mape_element import MapeElementTestCase
from .test_utils import UtilsTestCase


if __name__ == '__main__':
    rosunit.unitrun('test_mapek_framework',
                    'test_group_mapek_framework', GroupTestCase)
    rosunit.unitrun('test_mapek_framework',
                    'test_interaction_mapek_framework', InteractionTestCase)
    rosunit.unitrun('test_mapek_framework',
                    'test_managed_system_mapek_framework', ManagedSystemTestCase)
    rosunit.unitrun('test_mapek_framework',
                    'test_mape_element_mapek_framework', MapeElementTestCase)
    rosunit.unitrun('test_mapek_framework',
                    'test_utils_mapek_framework', UtilsTestCase)
