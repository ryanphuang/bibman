#!/usr/bin/env python
from bibtexparser.bparser import BibTexParser
import os,sys
import getopt
from bibwriter import normal_print

def parse(fname):
  of = open(fname, 'r')
  parser = BibTexParser(of)
  record_list = parser.get_entry_list()
  of.close()
  return record_list

def usage():
  print "Usage: %s [-e --exclude TAGLIST] [-i --include TAGLIST] [-r --replace TAGLIST] [-h --help] FILE\n\n" % sys.argv[0]
  print "\t\tExample: %s -r booktitle,series reference.bib > refshort.bib\n\n" % sys.argv[0]

if __name__ == '__main__':
  try:
    optlist, args = getopt.getopt(sys.argv[1:],"e:i:r:h", ["exclude=", "include=", "replace=", "help"])
  except getopt.GetoptError:
    usage()
    sys.exit(1)
  exclude = None
  include = None
  replace = None
  for opt,arg in optlist:
    if opt in ("-h", "--help"):
      usage()
      sys.exit(0)
    if opt in ("-e", "--exclude"):
      exclude = arg
    if opt in ("-i", "--include"):
      include = arg
    if opt in ("-r", "--replace"):
      replace = arg
  if len(args) == 0 or not os.path.isfile(args[0]):
    usage()
    sys.exit(1)
  if include and exclude:
    sys.stderr.write("Conflicting options: exclude, include\n")
    sys.exit(1)
  if replace and len(replace.split(',')) % 2 != 0:
    sys.stderr.write("Replace list must be even\n")
    sys.exit(1)
  fname = args[0]
  records = parse(fname)
  normal_print(records, include, exclude, replace)
