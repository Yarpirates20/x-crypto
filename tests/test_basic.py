#!/usr/bin/python3
""" Tests for xcrypt.py convert module """

import os
import re
from subprocess import getstatusoutput

from context import xcrypt

class TestBasic:
    """ Test the basic functionality of xcrypt """
    
    def test_exists(self):
        """ Program exists """
        assert os.path.isfile("./xcrypt/xcrypt.py")

    def test_usage(self):
        """ Usage"""
        pass

    def test_str_to_int(self):
        """ Test str_to_int """
        assert xcrypt.convert.text2int("Welcome to England!") == 1949000055819034788318500292382655163516478497



