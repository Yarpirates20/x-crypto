"""
Description
===========

Command superclass for all commands

Module Contents
===============

#TODO: add module contents

Examples
========

#TODO: add examples

"""
import argparse
import convert as convert

class Command:
    def __init__(self) -> None:
        pass

    def execute(self, options: argparse.Namespace) -> None:
        pass

class Convert(Command):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, options: argparse.Namespace) -> None:
        """ Execute the convert command """
        conversion_function = convert.type_to_function[options.type]

        result = conversion_function(options.input)
        convert.display_results(options.input, result)

def main() -> None:
    """ Main function """
    options1 = argparse.Namespace()
    command1 = Convert()
    command1.execute()

if __name__ == "__main__":
    main()

