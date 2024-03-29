#!/usr/bin/python3
"""
Input conversion module

SYNOPSIS
========

#TODO: enter synopsis here

DESCRIPTION
===========

This Python module, named 'convert', provides functionality to convert strings to integers and integers to strings, which is a common requirement in cryptography algorithms.

It includes two main functions: 
1. str_to_int: This function takes a string as input and attempts to convert it to an integer. This is often used when encoding plaintext into numeric form for encryption. If the conversion is successful, it returns the integer. If the string cannot be converted to an integer, it raises a ValueError.

2. int_to_str: This function takes an integer as input and converts it to a string. This is often used when decoding numeric ciphertext back into plaintext. It returns the resulting string.

These functions are crucial for the process of encryption and decryption in many cryptographic systems.

EXAMPLES
========

>>> import convert
>>> convert.str_to_int("Welcome to England!")
'1949000055819034788318500292382655163516478497'

"""
import argparse
import binascii
import os
import sys
from typing import List, Union

#--------------------------------------------------
def display_results(original_input: Union[str, int],
                    converted: Union[int, str] ) -> None:
    """ Display the results of the conversion to the user """

    print(f"\nOriginal input({type(original_input)}): {original_input}")
    print(f"Converted value({type(converted)}): {converted} ")

#--------------------------------------------------
def convert_output_type(output_type: str, result: Union[int, str]) -> Union[int, str]:
    """ Convert the result to the desired output type """
    if output_type == 'bin':
        return bin(result)
    elif output_type == 'hex':
        return hex(result)
    # elif output_type == 'int':
    #     return int(result)
    # elif output_type == 'base64':
    #     return binascii.b2a_base64(result)
    # elif output_type == 'str':
    #     return str(result)

def text2int(text: str) -> int:
    """ Converts a string to an integer """
    try:
        # convert string to hex
        hexstr = binascii.hexlify(text.encode('utf-8'))

        # convert hex to int
        integer_m = int(hexstr, 16)
        return integer_m
    except ValueError:
        raise ValueError(
            f"Error: '{text}' could not be converted to an integer")

#--------------------------------------------------
def int2text(integer: int) -> str:
    """ Converts an integer to a string """
    try:
        # convert int to hex
        back2hex = f"{int(integer):x}"

        # convert hex to string
        back2str = binascii.unhexlify(back2hex.encode('utf-8'))

        return back2str

    except ValueError:
        raise ValueError(
            f"Error: '{integer}' could not be converted to a string")

#--------------------------------------------------
def is_string_type(value: str) -> bool:
    """Check if a value is a string and not numeric"""
    try:
        float(value)
        return False
    except ValueError:
        return True


#--------------------------------------------------
def is_int_type(value: str) -> bool:
    """Check if a value is an integer"""
    try:
        int(value)
        return True
    except ValueError:
        return False

#--------------------------------------------------
# Map type names to functions
type_to_function = {'str': text2int, 'int': int2text}

#--------------------------------------------------
def get_options(argv: List[str] = sys.argv[1:]) -> argparse.Namespace:
    """ Get command line options """
    parser = argparse.ArgumentParser(prog='xcrypt')
    subparsers = parser.add_subparsers(title='subcommands',
                                       help='conversion operations')

    convert_parser = subparsers.add_parser('convert')


    convert_parser.add_argument('-t',
                                '--type',
                                action='store',
                                choices=list(type_to_function.keys()),
                                help='Type of input',
                                default='str')

    convert_parser.add_argument('input',
                                action='store',
                                help='Input to convert')
    # convert_parser.add_argument('-s',
    #                             '--string',
    #                             action='store',
    #                             type=string_type,
    #                             help='String to convert'
    #                             )


    convert_parser.add_argument('-o',
                                '--output',
                                action='store',
                                choices=['bin', 'hex'],
                                default='hex',
                                help='Output type')

    options = parser.parse_args(argv)

    return options

#--------------------------------------------------
# def convert_input(user_input: Union[str, int] )

#--------------------------------------------------
def main() -> None:
    """ Main function """
    options = get_options(sys.argv[1:])
    conversion_function = type_to_function[options.type]
    
    result = conversion_function(options.input)
    
    if options.output != 'str':
        result = convert_output_type(options.output, result)

    display_results(options.input, result)



#--------------------------------------------------
if __name__ == '__main__':
    main()
