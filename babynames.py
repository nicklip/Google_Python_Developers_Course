#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
   # Opening the file
  f = open(filename, 'rU')
  # Reading all of the lines
  lines = f.readlines()
  # Empty list to hold the year, names, and ranks
  ranks_names = []
  for line in lines:
    # search for the year
    year = re.search(r'\s(\d\d\d\d)</h3>', line)
    # if the year is found, append it to the list
    if year: 
      ranks_names.append(year.group(1))
    # search for the rank, male name, and female name
    rank_male_female = re.search(r'(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
    # If they are found then append the male name plus its rank, as well as the 
    # female name plus its rank
    if rank_male_female:
      ranks_names.append(rank_male_female.group(2) + ' ' + rank_male_female.group(1))
      ranks_names.append(rank_male_female.group(3) + ' ' + rank_male_female.group(1))
  # Sort the list alphabetically
  ranks_names.sort()
  # Return the list
  return ranks_names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for file in args:
    # Using the extract_names function to get the year, names, and ranks
    year_name_rank = extract_names(file)
    # Getting the year
    year = year_name_rank[0]
    # If summary is true, write the list (line by line) to a text file
    if summary == True:
      sum_file = open('summary_baby' + year + '.txt', 'w')
      for item in year_name_rank:
        sum_file.write("%s\n" % item)
      sum_file.close()
    # Otherwise print the list line by line
    else:
      for item in year_name_rank:
        print item
  
if __name__ == '__main__':
  main()





