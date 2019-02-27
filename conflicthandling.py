import csv
s1 = input('Please input the first file name:\n')
s2 = input('Please input the second file name:\n')
conflictLines = []
with open(s1, 'r') as csvfile1:
    with open(s2, 'r') as csvfile2:
        lines1 = csv.reader(csvfile1)
        lines2 = csv.reader(csvfile2)
        i = 0
        for line1, line2 in zip(lines1, lines2):
            i += 1
            if line1[2] != line2[2]:
                conflictInfo = ["The confilt appears at row {}, column 3".format(i + 1)]
                conflictLines.append(conflictInfo)
            if line1[3] != line2[3]:
                conflictInfo = ["The confilt appears at row {}, column 4".format(i + 1)]
                conflictLines.append(conflictInfo)
            if line1[4] != line2[4]:
                conflictInfo = ["The confilt appears at row {}, column 5".format(i + 1)]
                conflictLines.append(conflictInfo)

for line in conflictLines:
   print(line)

with open('ConflictInfo.csv', 'w', newline = '') as outfile:
    writer = csv.writer(outfile)
    for i in conflictLines:
        writer.writerow(i)