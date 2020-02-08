#import requests
#import xml.etree.ElementTree as ET
import pandas as pd

dict = {'testing': {'id': '1', 'name': 'luca', 'year': '1997'},
        'more': {'id': '2', 'name': 'mandy', 'year': '1998'}}

#sum(len(v) for v in food_colors.itervalues())
length = 0
for k, v in dict.items():
    print(len(dict[k].items()))
    length = len(dict[k].items())
lol2 = [[] for i in range(length)]
print(lol2)
