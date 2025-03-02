#!/usr/bin/env python

#-----------------------------------------------------------------------
# testregdetails.py
# Author: Bob Dondero (modified by you)
#-----------------------------------------------------------------------

import os
import sys
import argparse

#-----------------------------------------------------------------------

MAX_LINE_LENGTH = 72
UNDERLINE = '-' * MAX_LINE_LENGTH

#-----------------------------------------------------------------------

def parse_args():

    parser = argparse.ArgumentParser(
        description=
        "Test the Registrar's application's handling of " +
        "class details requests")
    parser.add_argument('program', metavar='program', type=str,
        help='the client program to run')
    parser.add_argument('host', metavar='host', type=str,
        help='the host on which the server is running')
    parser.add_argument('port', metavar='port', type=int,
        help='the port at which the server is listening')
    args = parser.parse_args()

    return (args.program, args.host, args.port)

#-----------------------------------------------------------------------

def print_flush(message):
    print(message)
    sys.stdout.flush()

#-----------------------------------------------------------------------

def exec_command(program, args):

    print_flush(UNDERLINE)
    command = 'python ' + program + ' ' + args
    print_flush(command)
    exit_status = os.system(command)
    if os.name == 'nt':  # Running on MS Windows?
        print_flush('Exit status = ' + str(exit_status))
    else:
        print_flush('Exit status = ' + str(os.WEXITSTATUS(exit_status)))

#-----------------------------------------------------------------------

def main():

    program, host, port = parse_args()

    # Test case 1: Display help for the client program.
    exec_command(program, '-h')

    prefix = host + ' ' + str(port) + ' '

    # Test case 2: Valid class request with a typical class number.
    exec_command(program, prefix + '8321')

    # Additional Test Cases:

    # Test case 3: Request details for another valid class number.
    exec_command(program, prefix + '1103')

    # Test case 4: Request details for a large class number.
    exec_command(program, prefix + '99999')

    # Test case 5: Request details for a very small class number.
    exec_command(program, prefix + '1')

    # Test case 6: Request details with a non-numeric class ID (invalid input).
    exec_command(program, prefix + 'ABC123')

    # Test case 7: Request details for a negative class ID (invalid input).
    exec_command(program, prefix + '-4321')

    # Test case 8: Request details with a missing class ID (invalid input).
    exec_command(program, prefix)

    # Test case 9: Request multiple class details simultaneously.
    exec_command(program, prefix + '8321 1103 2205')

    # Test case 10: Request details for a class that does not exist.
    exec_command(program, prefix + '0000')

if __name__ == '__main__':
    main()
