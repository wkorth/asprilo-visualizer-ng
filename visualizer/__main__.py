#!/usr/bin/env python

"""
An application for converting scenario files from movingai's .scen format file
to clingo's .lp format. Uses stdin and stdout by default.
"""

import argparse
import logging
import sys
import yaml
from PyQt5.QtWidgets import *
import solveutils, parseutils
from modelscene import ModelScene
from gui import MainWindow, ModelView


def get_args():
    """
    Defines and parses command line arguments.
    """

    parser = argparse.ArgumentParser(
        description="""
                    Visualizes a clingo model.
                    """)

    parser.add_argument(
        "-i", "--input", metavar="IN", type=argparse.FileType("r"),
        default=sys.stdin, help="read from file")

    parser.add_argument("-c", "--config", metavar="CFG",
                        type=argparse.FileType("r"), help="use YAML configuration file")

    return parser.parse_args()


def main():
    """
    Starts the application
    """

    args = get_args()

    app = QApplication(sys.argv)

    config = parseutils.parse_config(args.config)

    win = MainWindow()
    win.show()
    print(args.input)
    
    if args.input is not None:
        win.solve_and_add(args.input, config)
    
    app.exec()


if __name__ == "__main__":
    sys.exit(main())
