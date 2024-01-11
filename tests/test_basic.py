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