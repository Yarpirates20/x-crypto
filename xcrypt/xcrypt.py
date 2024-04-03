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
import convert_helpers
import Command
import Convert

def get_options(argv: List[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="xcrypt")
    subparsers = parser.add_subparsers()
    convert_parser = subparsers.add_parser("convert")
    Convert.arguments(convert_parser)

    options = parser.parse_args(argv)
    if "command" not in options:
        parser.error("No command given")
    
    return options

def main() -> None:
    """Main function"""
    options = get_options(sys.argv[1:])
    command = Convert()
    command.execute(options)


if __name__ == "__main__":
    main()
