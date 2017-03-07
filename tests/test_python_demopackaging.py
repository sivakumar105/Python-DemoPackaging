#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_demopackaging
----------------------------------

Tests for `python_demopackaging` module.
"""


import unittest

from python_demopackaging import python_demopackaging



class TestPython_demopackaging(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, World!"

    def tearDown(self):
        pass

    def test_prints_hello_world(self):
        output = python_demopackaging.hello()
        assert(output == self.hello_message)
