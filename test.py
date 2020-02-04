import requests
import xml.etree.ElementTree as ET
import pandas as pd

ids = [204505,229853]
format_ids = ','.join(map(str,ids))
link = "https://api.geekdo.com/xmlapi2/thing?id={}&stats=1".format(format_ids)
r = requests.get(link)
root = ET.fromstring(r.content)
#root2 = ET.parse(r.content)
data = {}
#for id in ids:
    #data[id] = {}


"""for child in root.iter('name'):
    if(child.get('type') == 'primary'):
        print(child.get('value'))

for child in root.iter('yearpublished'):
    print(child.get('value'))

for child in root.iter('minplayers'):
    print(child.get('value'))

for child in root.iter('maxplayers'):
    print(child.get('value'))

for child in root.iter('link'):
    if (child.tag == 'boardgamecategory'):
        print(child.get('value'))"""



"""for child, id in zip(root.iter('name'),ids):
    if(child.get('type') == 'primary'):
        data[id]['Name'] = child.get('value')"""


for item in root.findall('item'):
    id = item.get('id')
    playtime = []
    for x in item.iter('*'):
        if(x.tag == 'item'):
            data[id] = {}
        if(x.tag == 'name'):
            if(x.get('type') == 'primary'):
                data[id]['Name'] = x.get('value')
        elif(x.tag == 'yearpublished'):
            data[id]['Year'] = x.get('value')
        elif(x.tag == 'minplaytime'):
            playtime.append(x.get('value'))
        elif(x.tag == 'maxplaytime'):
            playtime.append(x.get('value'))
        elif(x.tag == 'minplayers'):
            data[id]['Min. Players']

        time = '-'.join(map(str,playtime))
        time = time + " min"
        data[id]['Playtime'] = time

print(data)




#more_root = r.getroot()
#for child in more_root.iter():
#    print(child.tag)
