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
from typing import List
import convert
import Command


def main() -> None:
    """Main function"""
    options = argparse.Namespace()
    command = Command.Convert()
    command.execute(options)


if __name__ == "__main__":
    main()
