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
import os
from typing import Union

def display_results(original_input: [str, int],converted: Union[int, str]) -> None: 
    """ Display the results of the conversion to the user """
    
    # Clear the screen
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux
        os.system('clear')

    print(f"\nOriginal input({type(original_input)}): {original_input}")
    print(f"Converted value({type(converted)}): {converted} ")

