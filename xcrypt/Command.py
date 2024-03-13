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
import sys
from typing import List
import convert as convert


class Command:

    @classmethod
    def arguments(cls, sub_parser: argparse.ArgumentParser) -> None:
        """Add command line arguments to parser"""
        pass

    def __init__(self) -> None:
        pass

    def execute(self, options: argparse.Namespace) -> None:
        pass


class Convert(Command):

    @classmethod
    def arguments(cls, convert_parser: argparse.ArgumentParser) -> None:
        convert_parser.add_argument(
            "-t",
            "--type",
            action="store",
            choices=list(convert.type_to_function.keys()),
            help="Type of input",
            default="str",
        )

        convert_parser.add_argument("input",
                                    action="store",
                                    help="Input to convert")

        convert_parser.add_argument(
            "-o",
            "--output",
            action="store",
            choices=["bin", "hex", "int", "base64", "str"],
            default="hex",
            help="Output type",
        )

        convert_parser.set_defaults(command=convert)

    def __init__(self) -> None:
        super().__init__()

    def execute(self, options: argparse.Namespace) -> None:
        """Execute the convert command"""
        conversion_function = convert.type_to_function[options.type]

        result = conversion_function(options.input)

        if options.output != 'str':
            result = convert.convert_output_type(options.output, result)

        convert.display_results(options.input, result)



def main() -> None:
    """Main function"""
    options1 = argparse.Namespace()
    command1 = Convert()
    command1.execute(options1)


if __name__ == "__main__":
    main()
