#!/usr/bin/env python3.7
from argparse import ArgumentParser


parser = ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial (or complete) string to search')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()

matches = [word for word in words if word.lower().strip() in snippet]
print(matches)
