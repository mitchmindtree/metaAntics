#!usr/bin/env python2


'''

Meta Antics.

A python program for experimenting with large amounts of music metadata!

Usage:
    metaAntics.py [-h | --help] [-v | --version] [--uj --gmst --gmar --fdg]

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    --uj            Update the entire music meta database.
    --gmst          Update the Google Music 'stations' JSON database.
    --gmar          Update the Google Music 'artists' JSON database.
    --fdg           Create a Force Directed Graph of your Google Music Artists and their relationships

'''


import sys, argparse, os
from docopt import docopt
from pprint import pprint
from gmusicapi import Mobileclient
from operator import attrgetter, itemgetter
from gmusicMeta import loadGmusicMeta, updateGmusicMeta


def getMenu():
    return {
            '1' : "Update the entire music meta database.",
            '2' : "Update the Google Music 'stations' JSON database.",
            '3' : "Update the Google Music 'artists' JSON database.",
            '0' : "EXIT"
            }


def initArgs(args):
    for arg in args:
        arg = False


def menuDisplay(args):
    menu = getMenu()
    while True:
        initArgs(args)
        print("\nMENU:")
        pprint(menu) 
        sel = raw_input("Enter your selection: ")
        if sel == '0':
            sys.exit(0)
        elif sel == '1': 
            updateGmusicMeta(True, True)
        elif sel == '2':
            updateGmusicMeta(True, False)
        elif sel == '3':
            updateGmusicMeta(False, True)


def main():
    args = docopt(__doc__, version='Meta Antics (experimental stage)')
    if args['--uj']:
        updateGmusicMeta(True, True)
    if args['--gmar']:
        updateGmusicMeta(True, False) 
    if args['--gmst']:
        updateGmusicMeta(False, True) 
        print("There's yo shizz nigga!")
    menuDisplay(args)
        

if __name__ == "__main__":
    main() 

