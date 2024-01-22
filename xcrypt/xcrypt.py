#!/usr/bin/env python3
"""
Cryptography CLI toolbox

SYNOPSIS
========

::
    
        xcrypt [OPTION]... [FILE]...

DESCRIPTION
===========

#TODO: xcrypt is a CLI toolbox for cryptography. It provides a set of tools

EXAMPLES
========


"""

import sys
import os

import argparse
import convert, Command



def main() -> None:
    """ Main function """
    options1 = argparse.Namespace()
    command1 = Command.Convert()
    command1.execute(options1)

if __name__ == "__main__":
        main()