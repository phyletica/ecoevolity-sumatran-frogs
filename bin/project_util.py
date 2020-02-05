#! /usr/bin/env python

import os
import sys

BIN_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.dirname(BIN_DIR))
ECOEVOLITY_ALIGNMENT_DIR = os.path.join(PROJECT_DIR, "alignments")
ECOEVOLITY_CONFIG_DIR = os.path.join(PROJECT_DIR, "ecoevolity-configs")
ECOEVOLITY_SIM_DIR = os.path.join(PROJECT_DIR, "ecoevolity-simulations")

def main():
    sys.stdout.write("{0}\n".format(PROJECT_DIR))

if __name__ == '__main__':
    main()

