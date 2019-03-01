#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Tags Maker
Usage:
  tagmaker <src> <out> <tag> <encode>
"""
from docopt import docopt
import csv
import os
import time
if __name__ == '__main__':
  args = docopt(__doc__)
  print(args)
  if args['<src>'] == args['<out>']:
    exit
  with open(args['<src>'],mode='r',encoding=args['<encode>']) as src:
    with open(args['<out>'],mode='w',encoding=args['<encode>'],newline='') as out:
      ls = csv.reader(src)
      writer = csv.writer(out)
      sum = 0
      for l in ls:
        if l[2]:
          while len(l) < 5:
            l.append(l[len(l)-1])
          if l[4] == '':
            l[4] = args['<tag>']
            sum += 1
        writer.writerow(l)
