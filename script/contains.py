#!/usr/bin/env python3.7
from argparse import ArgumentParser


parser = ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial (or complete) string to search')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

matches = []

for word in words:
    if snippet in word.lower().strip():
        matches.append(word.lower().strip())

print(matches)
