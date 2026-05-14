import re

fileInp = open('testData.txt');

count = 0


for line in fileInp:
    lineNum = re.findall('[0-9]+',line)
    for num in lineNum:
        count += int(num)


print(count)
