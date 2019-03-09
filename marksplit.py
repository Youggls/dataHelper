#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Mark Split
Usage:
  marksplit <src> <mark> <item> <encode>
"""
from docopt import docopt
import csv
import os
import time

def marksplit(src,mark,item,encode):
  date = time.strftime('%Y%m%d',time.localtime(time.time()))
  tmpname = item+'-'+date+'.csv'
  with open(src,mode='r',encoding=encode) as src:
    with open(tmpname,mode='w',encoding=encode,newline='') as out:
      ls = csv.reader(src)
      writer = csv.writer(out)
      sum =0
      for l in ls:
        if len(l) >= 6:
          if l[5] == mark:
            sum += 1
            writer.writerow([l[0],l[1],l[2],l[3],l[4]])
    outname = item+'-'+str(sum)+'-'+date+'.csv'
    os.rename(tmpname,outname)

if __name__ == '__main__':
  args = docopt(__doc__)
  print(args)
  marksplit(args['<src>'],args['<mark>'],args['<item>'],args['encode'])
