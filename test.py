inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
res = []
for line in inFile:
    tmpLine = line.split()
    if len(tmpLine) != 0:
        res.append((tmpLine[0], tmpLine[1], tmpLine[3]))
res.sort()
for line in res:
    print(*line, file=outFile)
inFile.close()
outFile.close()
