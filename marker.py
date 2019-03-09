#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Marker
Usage:
  marker <src> <out> <mark> <encode>
"""
from docopt import docopt
import csv
import time
def marker(src,out,mark,encode):
  with open(src,mode='r',encoding=encode) as src:
    with open(out,mode='w',encoding=encode,newline='') as out:
      ls = csv.reader(src)
      writer = csv.writer(out)
      sum = 0
      for l in ls:
        if l[2]:
          while len(l) < 6:
            l.append(l[len(l)-1])
          if l[5] == '':
            l[5] = mark
            sum += 1
        writer.writerow(l)

if __name__ == '__main__':
  args = docopt(__doc__)
  print(args)
  if args['<src>'] == args['<out>']:
    print('error: out file can not be src file')
    exit
  marker(args['<src>'],args['<out>'],args['<mark>'],args['<encode>'])
