#!/usr/bin/env python


import argparse
import json

parser = argparse.ArgumentParser(prog="test")
parser.add_argument("--json", type=json.loads)


args = parser.parse_args()
print(args.json)
