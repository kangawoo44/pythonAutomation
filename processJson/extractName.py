file_object = open("./HotelFacilityTypes_enumSource.txt", 'r')
outfile = open("extractedNames.txt", 'w+')
for line in file_object:
    newLine = line.replace("symbol (", "")
    newLine = newLine.replace(")", "")
    outfile.write(newLine)
            
file_object.close()
outfile.close()