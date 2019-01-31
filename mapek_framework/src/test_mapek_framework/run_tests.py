#!/usr/bin/env python
import unittest
import rosunit
from .test_group import GroupTestCase


if __name__ == '__main__':
    rosunit.unitrun('test_mapek_framework',
                    'test_group_mapek_framework', GroupTestCase)
