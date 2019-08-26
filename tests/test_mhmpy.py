# -*- coding: utf-8 -*-
"""
This is the unittest for mhmpy.
"""
from __future__ import division, absolute_import, print_function

import unittest
from mhmpy import __version__


class TestOGS(unittest.TestCase):
    def setUp(self):
        self.version = __version__

    def test_mhmpy(self):
        print(self.version)


if __name__ == "__main__":
    unittest.main()
