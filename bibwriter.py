#!/usr/bin/env python

def _key_val_print(k, v, inclist, exlist):
  if (len(inclist) == 0 and len(exlist) == 0) or (len(inclist) != 0 and k in inclist) \
    or (len(exlist) != 0 and k not in exlist):
    print " %s = {%s}," % (k, v)

def normal_print(records, include=None, exclude=None, replace=None):
  inclist = []
  exlist = []
  rplist = []
  if include:
    if exclude:
      return
    inclist = include.split(',')
  elif exclude:
    exlist = exclude.split(',')
  if replace:
    rplist = replace.split(',')
  rplan = len(rplist)
  if rplan % 2 != 0:
    return
  for record in records:
    print "@%s{%s," % (record['type'], record['id'])
    rec = None
    if rplan != 0:
      for i in range(0, rplan, 2):
        if record.has_key(rplist[i]) and record.has_key(rplist[i + 1]):
          if rec is None:
            rec = record.copy()
          rec[rplist[i]] = rec[rplist[i + 1]]
          rec[rplist[i + 1]] = ''
    if rec is None:
      rec = record
    for k,v in rec.items():
      if k == 'type' or k == 'id' or len(v.strip()) == 0:
        continue
      _key_val_print(k, v, inclist, exlist)
    print "}"
