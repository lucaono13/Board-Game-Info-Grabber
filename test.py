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
    for x in item.iter('*'):
        #print(x.tag)
        if(x.tag == 'image'):
            print(x.text)
