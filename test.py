inFile = open('input.txt', 'r', encoding='utf-8-sig')
outFile = open('output.txt', 'w', encoding='utf8')
marks = []
k = 0
for line in inFile:
    tmpLine = line.split()
    if len(tmpLine) == 1:
        k = int(tmpLine[0])
    elif len(tmpLine) > 1:
        b1 = int(tmpLine[-1])
        b2 = int(tmpLine[-2])
        b3 = int(tmpLine[-3])
        if b1 >= 40 and b2 >= 40 and b3 >= 40:
            marks.append(b1 + b2 + b3)
marks.sort(reverse=True)
ans = -1
if len(marks) <= k:
    ans = 0
else:
    bk = marks[k]
    marks1 = marks[:k]
    marks1.sort()
    if bk == marks1[-1]:
        ans = 1
    else:
        for i in range(k):
            if i == 0:
                if marks1[0] > bk:
                    ans = marks1[0]
                    break
            else:
                if marks1[i] > marks1[i - 1]:
                    ans = marks1[i]
                    break
print(ans, file=outFile)
inFile.close()
outFile.close()
