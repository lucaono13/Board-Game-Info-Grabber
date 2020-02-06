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

for item in root.findall('item'):
    votes = {}
    for x in item.iter('poll'):
        if(x.get('name') == 'suggested_numplayers'):
            #votes = {}
            for j in x.findall('results'):
                for k in j.iter('result'):
                    if(k.get('value') == 'Best'):
                        votes[j.get('numplayers')] = int(k.get('numvotes'))

    print(votes)
    print(max(votes, key=votes.get))
