#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

''' 1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word. '''

def print_words(filename):
  # Opening the file and reading it in as one big string
  f = open(filename, 'rU')
  lines = f.read()
  # Making it lowercase
  lines = lines.lower()
  # Taking out any endlines or symbols that are not letters
  lines = lines.replace('\n', ' ')
  lines = lines.replace('"', '')
  lines = lines.replace(',', '')
  lines = lines.replace("'", '')
  lines = lines.replace('.', '')
  lines = lines.replace('?', '')
  lines = lines.replace(';', '')
  lines = lines.replace('--', ' ')
  lines = lines.replace('!', '')
  lines = lines.replace(':', '')
  lines = lines.replace(')', ' ')
  lines = lines.replace('(', ' ')
  lines = lines.replace('`', '')

  # Splitting the string into a list of words
  words = lines.split()
  # Creating empty dict and setting the counter to 0
  counts = {}
  i = 0
  for word in words:
    i += 1
    # If the word is already in the dict, move on to the next one
    if word in counts:
      continue
    # Otherwise create a new key in the dict for the word and set count = 1
    counts[word] = 1
    # New list of other words that are in front of word of interest
    other_words = words[i:]
    for other_word in other_words:
      # If this other word is equal to the word of interest increment the count
      if other_word == word:
        counts[word] += 1
      # Print all keys and counts, sorted by first letter of key
  for key in sorted(counts):
      print key, counts[key]


''' 2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace. '''

def print_top(filename):
  # Opening the file and reading it in as one big string
  f = open(filename, 'rU')
  lines = f.read()
  # Making it lowercase
  lines = lines.lower()
  # Taking out any endlines or symbols that are not letters
  lines = lines.replace('\n', ' ')
  lines = lines.replace('"', '')
  lines = lines.replace(',', '')
  lines = lines.replace("'", '')
  lines = lines.replace('.', '')
  lines = lines.replace('?', '')
  lines = lines.replace(';', '')
  lines = lines.replace('--', ' ')
  lines = lines.replace('!', '')
  lines = lines.replace(':', '')
  lines = lines.replace(')', ' ')
  lines = lines.replace('(', ' ')
  lines = lines.replace('`', '')
  # Splitting the string into a list of words
  words = lines.split()
  # Creating empty dict and setting the counter to 0
  counts = {}
  i = 0
  for word in words:
    i += 1
    # If the word is already in the dict, move on to the next one
    if word in counts:
      continue
    # Otherwise create a new key in the dict for the word and set count = 1
    counts[word] = 1
    # New list of other words that are in front of word of interest
    other_words = words[i:]
    for other_word in other_words:
      # If this other word is equal to the word of interest increment the count
      if other_word == word:
        counts[word] += 1
      # list of words (the keys), ordered from highest to lowest
  words_sorted = sorted(counts, key=counts.get, reverse=True)
  # Print the 20 words with the most counts
  for i in range(20):
      print words_sorted[i]
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
