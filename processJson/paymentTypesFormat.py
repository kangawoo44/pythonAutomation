import json

with open("./paymentTypes.json", "r") as json_file:
    data = json.load(json_file)
    with open('paymentTypesFormatted.json', 'w+') as outfile:
        for t in data['result']:
            payment_id = t['payment_id']
            name = t['name']
            eachLine = str(payment_id) + ': ' + '\'' + name + '\','
            # eachLine = str(type_id) + ': ' + '\'' + name + '\','
            outfile.write(eachLine + '\n')
json_file.close()