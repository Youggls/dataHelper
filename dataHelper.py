
#使用说明:输入路径并且输入修改模式:D(默认)   C(多写了分号的情况)
import csv
filepath=input('请输入文件路径:')
filename=input('请输入修改后的文件名:')
csv_file=csv.reader(open(filepath,'r'))
out=open(filename+'.csv','w',newline='')
csv_write=csv.writer(out)
tot=0
#对字符串进行处理
def standardize(char):
    #可能需要替换中文分号
    char=char.replace('；',' ')
    #多写了英文分号的情况
    char=char.replace(';',' ')
    #先把前后空格消去
    char.strip()
    #处理字符之间的空格
    return ';'.join(char.split())
for content in csv_file:
    if content[2]!='':
        for i in range(2,5):
            content[i]=standardize(content[i])
        print(content)
        csv_write.writerow(content)
        tot=tot+1
print(tot)




