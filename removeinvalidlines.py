import csv
s = input("please input the file name:\n")
ss = input("please input the output file name\n")
totalNumber = 0
with open(s, 'r') as file:
    with open(ss, 'w', newline = '') as outfile:
        lines = csv.reader(file)
        writer = csv.writer(outfile)
        for line in lines:
            if(line[2]):
                totalNumber += 1
                writer.writerow(line)

file.close()
outfile.close()
print('total lines:', totalNumber)