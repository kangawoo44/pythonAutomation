def addSpaceAtCapitals(str):
    spacedStrList = []
    spacedStr = ""
    for index,ele in enumerate(str):
        if index == 0:
            lastCapitalIndex = 0
        if ele.isupper() and index != 0:
            spacedStrList.append(str[lastCapitalIndex:index])
            lastCapitalIndex = index
        if index == len(str) -1:
            spacedStrList.append(str[lastCapitalIndex:])

    if len(spacedStrList) == (0 or 1):
        spacedStr = str
    else:
        spacedStr = " ".join(spacedStrList)
    return spacedStr

file_object = open("./extractedNames.txt", 'r')
outfile = open("vocabs.txt", 'w+')
for line in file_object:
    lineStr = line.replace('\n', '')
    newLine = '\"' + lineStr + '\"' + ' { \"'
    spacedLine = addSpaceAtCapitals(lineStr)
    # print(spacedLine)
    newLine += spacedLine + '\" }\n'
    outfile.write(newLine)
            
file_object.close()
outfile.close()