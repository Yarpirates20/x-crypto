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
        
        # for flag in ["-h", "--help"]:
        #     rv, out = getstatusoutput(f"./xcrypt/xcrypt.py {flag}")
        #     assert rv == 0
        #     assert re.match("usage", out, re.IGNORECASE)
        pass 



#--------------------------------------------------
class TestConvert:
    """ Test the convert module """

    def test_exists(self):
        """ Module exists """
        assert os.path.isfile("./xcrypt/convert.py")

    def test_text2int(self):
        """ Test text2int """
        assert xcrypt.convert.text2int("Welcome to England!") == 1949000055819034788318500292382655163516478497

        assert xcrypt.convert.text2int("Hello") == 310939249775

    def test_int2str(self):
        """ Test int2str """
        assert xcrypt.convert.int2text(1949000055819034788318500292382655163516478497) == b'Welcome to England!'

        assert xcrypt.convert.int2text(310939249775) == b'Hello'


