#!/usr/zsh/env python3
# Import the argparse library
import argparse
import pprint
import webbrowser
from typing import Optional
from typing import Sequence
import os
import sys
from time import sleep
def open_chapter(link, number, sleep_time):
    webbrowser.open_new_tab(link + str(number))
    sleep(sleep_time)
def main(argv: Optional[Sequence[str]] = None)->int:
    parser = argparse.ArgumentParser()

    #positional
    parser.add_argument('website')
    parser.add_argument('start',type = int)
    parser.add_argument('end', type = int)
    parser.add_argument('sleep_time', type = int,help = "in seconds")



    args = vars(parser.parse_args(argv))
    for i in range(args['start'],args['end']+1):
        open_chapter(args['website'],i,args['sleep_time'])







    return 0




def run():
    exit(main())
if __name__ == '__main__':
    run()