import csv
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('The args ie too less!')
        exit
    
    srcfile = sys.argv[1]

    with open(srcfile, 'r') as f:
        lines = csv.reader(f)
        with open('fix.csv', 'w', newline='') as out:
            writer = csv.writer(out)
            for line in lines:
                aspect1 = line[2].split(';')
                aspect2 = line[5].split(';')
                flag = False
                if ((len(aspect1) == 1) and (len(aspect2) >= 2)):
                    if (aspect1[0] in aspect2) == True:
                        flag = True
                if ((len(aspect1) == 1) and (len(aspect2) == 1)):
                    if (aspect1[0] != aspect2[0]) == True:
                        flag = True
                if flag:
                    line[11] = '0'

                writer.writerow(line)
        out.close()
    f.close()