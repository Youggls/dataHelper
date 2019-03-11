
"""Merge
Usage:
    merge <filename1> <filename2> <outputname>
"""
import csv
import sys
#打印提示信息
def printInfos(str):
    print('[INFO]: ' + str)
#打印content有冲突信息
def printConflicts(row, column):
    print('[INFO]: WARNIGNS! The content is different at row {}, column {}'.format(row, column))

def judgeLen(list1, list2, list3):
    if len(list1) != len(list2):
        return False
    elif len(list1) != len(list3):
        return False
    elif len(list2) != len(list3):
        return False
    else:
        return True

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        printInfos("args is less than 2, please try again")
        sys.exit()

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if len(sys.argv) == 4:
        output = sys.argv[3]
    else:
        output = "out.csv"

    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            with open(output, 'w', newline = '') as out:
                lines1 = csv.reader(f1)
                lines2 = csv.reader(f2)
                writer = csv.writer(out)

                outLine = []

                row = 0
                for l1, l2 in zip(lines1, lines2):
                    row += 1
                    #判断content内容是否一样,不一样中止
                    if(l1[1] != l2[1]):
                        printConflicts(row, 2)
                        sys.exit()
                    
                    #写入行标
                    outLine.append("{}".format(row))
                    #写入content
                    outLine.append(l1[1])

                    outLine.append(l1[2])
                    outLine.append(l1[3])
                    outLine.append(l1[4])
                    outLine.append(l2[2])
                    outLine.append(l2[3])
                    outLine.append(l2[4])
                    #分割情感词等
                    aspect1 = l1[2].split(';')
                    aspect2 = l2[2].split(';')

                    sentiment1 = l1[3].split(';')
                    sentiment2 = l2[3].split(';')

                    polarity1 = l1[4].split(';')
                    polarity2 = l2[4].split(';')

                    #判断内容aspect、情感词、极性是否不匹配，不一样中止
                    if (judgeLen(aspect1, sentiment1, polarity1) == False):
                        printInfos('WARNING! The length of info in file1 is different at line {}'.format(row))
                        sys.exit()
                    elif (judgeLen(aspect1, sentiment1, polarity1) == False):
                        printInfos('WARNING! The length of info in file2 is different at line {}'.format(row))
                        sys.exit()
                    
                    outAspect = str()
                    outPolarity = str()
                    outSentiment = str()
                    count = 0
                    for i in range(0, len(aspect1)):
                        if (aspect1[i] in aspect2) == False:
                            continue
                        #确保完全一样的情感词、极性、aspect才能被写入
                        if (sentiment1[i] in sentiment2) and (polarity1[i] in polarity2):
                            if len(outAspect) == 0: 
                                outAspect += aspect1[i]
                                outPolarity += polarity1[i]
                                outSentiment += sentiment1[i]
                                count += 1
                            else:
                                outAspect += (';' + aspect1[i])
                                outPolarity += (';' + polarity1[i])
                                outSentiment += (';' + sentiment1[i])
                                count += 1

                    outLine.append(outAspect)
                    outLine.append(outSentiment)
                    outLine.append(outPolarity)

                    if ((count != len(aspect1)) or (count != len(aspect2))):
                        outLine.append("{}".format(0))
                    else:
                        outLine.append("{}".format(1))

                    writer.writerow(outLine)
                    outLine.clear()

                out.close()
            f2.close()
        f1.close()