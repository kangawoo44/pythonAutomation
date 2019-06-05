import json

data = []
# with open("./HotelFacilityTypes_enumSource.txt", 'r') as file_object:
    # line = file_object.readline()
file_object = open("./HotelFacilityTypes_enumSource.txt", 'r')
# with open('HotelFacilityTypesVocab.txt', 'w') as outfile:
outfile = open("HotelFacilityTypesVocab.txt", 'w+')
for line in file_object:
    vocabLine = '\"' + line + '\"' + '{ \"' + line + '\" }'
    outfile.write(vocabLine + '\n')
            

        # with open('HotelFacilityTypesVocab.txt', 'w') as outfile:
            # for t in data['result']:
            #     # type_id = t['room_facility_type_id']
            #     name = t['name']
            #     eachLine = '\"' + name + '\"'
            #     # eachLine = str(type_id) + ': ' + '\'' + name + '\','
            #     outfile.write(eachLine + '\n')
file_object.close()
outfile.close()