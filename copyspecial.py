#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise

The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" 
file is one where the name contains the pattern __w__ somewhere, where the w is one or more word chars. 
The provided main() includes code to parse the command line arguments, but the rest is up to you. Write
 functions to implement the features below and modify main() to call your functions.

Suggested functions for your solution(details below):

get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
copy_to(paths, dir) given a list of paths, copies those files into the given directory
zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
"""

def get_special_paths(the_dir):
  '''
  returns a list of the absolute paths of the special files 
  in the given directory
  '''
  the_paths = []
  # Getting the filenames from the directory
  filenames = os.listdir(the_dir)
  for filename in filenames:
    # Finding all of the "special" files
    special = re.findall(r'__\w+__', filename)
    if special:
      # Putting all special files in a list
      abs_path = os.path.abspath(os.path.join(the_dir, filename))
      the_paths.append(abs_path)
      # Returning list of special files
  return the_paths

def copy_to(paths, to_dir):
  '''
  given a list of paths, copies those files into the given directory
  '''
  # If the directory to copy the files to doesn't exist, create it
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    # Getting the files to be copied from each path
    filenames = os.listdir(path)
    for filename in filenames:
      # Getting the full path of each file
      abs_path = os.path.abspath(os.path.join(path, filename))
      # Copying each file to the desired directory
      if os.path.isfile(abs_path):
        shutil.copy(abs_path, to_dir)


def zip_to(paths, to_zip):
  '''
  given a list of paths, zip those files up into the given zipfile
  '''
  files = []
  for path in paths:
    # Getting the filenames from each path
    filenames = os.listdir(path)
    for filename in filenames:
      # Putting each joined path + filename into a list
      files.append(os.path.join(path,filename))
      # Command to zip the files into a zipfile with the desired name/path
  cmd = 'zip -j' + ' ' + to_zip + ' ' + ' '.join(files)
  # A warning to the user of what command is about to run
  print 'Command to run:', cmd 
  # Running the zip command
  (status, output) = commands.getstatusoutput(cmd)
  # If an error happens, print it to the terminal
  if status:
    sys.stderr.write(output)
    sys.exit(1)
      



def main():
  # This basic command line argument parsing code is provided. Add code to call your functions below.
  # Make a list of command line arguments, omitting the [0] element which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line or left as the empty string.
  # The args array is left just containing the directories (paths)
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  # If no arguments, print an error
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  ## Call your functions
  # If '--todir' command is called in the args, run the function to copy all of the 
  # files from all the paths to the desired directory.
  if todir:
    copy_to(args[0:len(args)], todir)
  # If '--tozip' command is called in the args, run the function to create a zip file,
  # with the desired name, of all of the files from all the paths.
  elif tozip:
    zip_to(args[0:len(args)], tozip)
  # Run the function to print all special files from all paths, if no '--todir' or 
  # '--to zipfile' command is included in the args
  else:
    paths = []
    for dirname in args:
      paths.extend(get_special_paths(dirname))
    print '\n'.join(paths)
  
if __name__ == "__main__":
  main()
