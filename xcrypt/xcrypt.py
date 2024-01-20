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

import convert, Command



def main() -> None:
    """ Main function """
    command1 = Command.Convert()
    command1.execute()

if __name__ == "__main__":
        main()