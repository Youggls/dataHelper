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
if __name__ == '__main__':
  args = docopt(__doc__)
  print(args)
  date = time.strftime('%Y%m%d',time.localtime(time.time()))
  tmpname = args['<item>']+'-'+date+'.csv'
  with open(args['<src>'],mode='r',encoding=args['<encode>']) as src:
    with open(tmpname,mode='w',encoding=args['<encode>'],newline='') as out:
      ls = csv.reader(src)
      writer = csv.writer(out)
      sum =0
      for l in ls:
        if len(l) >= 6:
          if l[5] == args['<mark>']:
            sum += 1
            writer.writerow([l[0],l[1],l[2],l[3],l[4]])
    outname = args['<item>']+'-'+str(sum)+'-'+date+'.csv'
    os.rename(tmpname,outname)