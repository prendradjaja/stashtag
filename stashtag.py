#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--branch-defaults", action="store_true",
        help="Display branch defaults")
args = parser.parse_args()

print(args.branch_defaults)
