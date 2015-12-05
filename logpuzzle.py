#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urlparse

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # Getting the server name from the filename
  server = re.search(r'_([\w.-]+)', filename)
  # Opening the file
  f = open(filename, 'rU')
  # Reading all of the lines
  lines = f.readlines()
  # Empty list to hold the puzzle urls
  puzzle_urls = []
  for line in lines:
    # search for the puzzle url in each line
    url = re.search(r'GET (\S+puzzle\S*) HTTP', line)
    #if the url exists in the line and it isn't a duplicate, concatenate it with the 
    # http:// and the server name, then add it to the list
    if url and 'http://' + server.group(1) + url.group(1) not in puzzle_urls:
      puzzle_urls.append('http://' + server.group(1) + url.group(1))
    else:
      pass
  # Function for custom sorting, sorts by second word in filename
  def MyFn(s):
    second_word = re.search(r'p-\w+-(\w+)\.jpg', s)
    return second_word.group(1)
  # if the url ends in the pattern "p-wordchars-wordchars.jpg", sort it by the second
  # word in the filename
  if re.search(r'p-\w+-\w+', puzzle_urls[0]):
    puzzle_urls = sorted(puzzle_urls, key=MyFn)
  # Else do a standard sort 
  else:
    puzzle_urls.sort()
  # Return all the urls
  return puzzle_urls


  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  # If the destination directory doesn't exist, create it
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  i = -1
  directories = []
  # Getting the full path of the directory
  the_dir = os.path.abspath(dest_dir)
  for img_url in img_urls:
    i += 1
    print "Retrieving... " + img_url
    # Concatenating the full path with the new filename for each url (img0, img1, etc.)
    full_dir = the_dir + '/img' + str(i)
    # Adding the full filename path to the directories list
    directories.append(full_dir)
    # Downloading each url to the full filename path
    urllib.urlretrieve(img_url, full_dir)
  # Creaing a html file of the image urls so that the image urls form a full picture
  # that can be viewed in a browser
  html_file = open(the_dir + '/index.html', 'w')
  html_file.write('<verbatim>\n<html>\n<body>\n')
  for direc in directories:
    html_file.write('<img src="' + direc + '" >')
  html_file.write('\n</body>\n</html>')
  html_file.close()




def main():
  # Getting the args
  args = sys.argv[1:]
  # If no args, print an error
  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)
  # Getting the desired directories for the urls to be copied into when the '--todir'
  # option command is in the args
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  # Getting the sorted image urls from the log files, using the img_urls function
  img_urls = read_urls(args[0])
  # If the '--todir' option command is in the args, download all of the image urls
  # and create an html file of the joined image urls using the download_images function
  if todir:
    download_images(img_urls, todir)
  # Otherwise just print the sorted image urls to the terminal
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
