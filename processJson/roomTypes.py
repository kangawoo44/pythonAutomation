import json

with open("./RoomFacilityTypes_source.json", "r") as json_file:
    data = json.load(json_file)
    with open('roomFacilityTypes.json', 'w+') as outfile:
        for t in data['result']:
            type_id = t['room_facility_type_id']
            name = t['name']
            eachLine = 'symbol (' + name + ')'
            # eachLine = str(type_id) + ': ' + '\'' + name + '\','
            outfile.write(eachLine + '\n')
json_file.close()