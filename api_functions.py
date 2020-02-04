import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Query the API to get basic info of board game (name, year, uid, type)
def query(search, gameCheck, expanCheck):
    link = ""
    if((gameCheck == True) & (expanCheck == False)):
        link = "https://api.geekdo.com/xmlapi2/search?query={}&type=boardgame".format(search)
    elif((gameCheck == False) & (expanCheck == True)):
        link = "https://api.geekdo.com/xmlapi2/search?query={}&type=boardgameexpansion".format(search)
    elif((gameCheck == True) & (expanCheck == True)):
        link = "https://api.geekdo.com/xmlapi2/search?query={}&type=boardgame,boardgameexpansion".format(search)
    else:
        link = "https://api.geekdo.com/xmlapi2/search?query={}".format(search)

    r = requests.get(link)
    root = ET.fromstring(r.content)

    name = []
    id = []
    year = []
    type = []
    nkids = 0

    for child in root.iter('*'):
        if(child.tag == 'item'):
            id.append(child.get('id'))
            type.append(child.get('type'))
        for primary in child.findall('name'):
            name.append(primary.get('value'))
        for x in child:
            for j in x:
                nkids += 1
            if(nkids == 1):
                year.append("NA")
            elif(nkids == 2):
                for pub in x.findall('yearpublished'):
                    year.append(pub.get('value'))
            #print(x)
            nkids=0

    #print(nchild)
    """
    for i in range(len(name)):
        print(name[i] + ", " + year[i] + ": " + id[i] + "; " + type[i])
    """
    type2 = [t.replace('boardgameexpansion','Board Game Expansion') for t in type]
    type2 = [t.replace('boardgameaccessory','Board Game Accessory') for t in type2]
    type2 = [t.replace('boardgame','Board Game') for t in type2]
    type2 = [t.replace('rpgitem','RPG Item') for t in type2]
    type2 = [t.replace('videogame','Video Game') for t in type2]

    #pics = getBoxArt(id)



    return(name, year, id, type2)

# Get the box art for each result
def getBoxArt(ids):
    joined_ids = ','.join(map(str,ids))

    image_urls = []
    link = "https://api.geekdo.com/xmlapi2/thing?id={}&stats=1".format(joined_ids)

    np_img = 0
    r = requests.get(link)
    root = ET.fromstring(r.content)
    no_image = 'https://upload.wikimedia.org/wikipedia/commons/0/0a/No-image-available.png'
    tags = []
    for item in root.findall('item'):
        for x in item.iter('*'):
            tags.append(x.tag)
            if(x.tag == 'image'):
                image_urls.append(x.text)
        if('image' not in tags):
            image_urls.append(no_image)
        else:
            pass
        tags=[]

    print("Box Art acquired")

    return image_urls

# Gets basic info for export: year, name, min and max players, and link to BGG site.
def getInfo(csv, ids, df):

    format_ids = ','.join(map(str,ids))
    link = "https://api.geekdo.com/xmlapi2/thing?id={}&stats=1".format(format_ids)
    url, name, year, min, max = ([] for i in range(5))
    r = requests.get(link)
    root = ET.fromstring(r.content)


    for i in ids:
        url.append("https://boardgamegeek.com/boardgame/{}".format(i))
    for child in root.iter('*'):
        if(child.tag == 'yearpublished'):
            year.append(child.get('value'))
            #df = df.append({'Year':child.get('value')},ignore_index=True)
        elif (child.tag =='name'):
            if(child.get('type') == 'primary'):
                name.append(child.get('value'))
                #df = df.append({'Name':child.get('value')},ignore_index=True)
        elif(child.tag == 'minplayers'):
            min.append(child.get('value'))
            #df = df.append({'Min. Players': child.get('value')},ignore_index=True)
        elif(child.tag == 'maxplayers'):
            max.append(child.get('value'))
            #df = df.append({'Max Players': child.get('value')},ignore_index=True)
        else: pass

    for i in range(len(url)):
        df = df.append({'Name':name[i],'Year':year[i],'Min. Players':min[i], 'Max Players':max[i], 'Link':url[i]}, ignore_index=True)
    return df


def grabInfo(info, ids):
    format_ids = ','.join(map(str,ids))
    link = "https://api.geekdo.com/xmlapi2/thing?id={}&stats=1".format(format_ids)
    lol = []
    tin = {}
    expdata = {}


    for i in info:
        #print(info[i])
        if(info[i] == True):
            lol.append(i)

    gamedata = {x for x in lol}
    #print(gamedata)

    r = requests.get(link)
    root = ET.fromstring(r.content)
    print(info)
    print(lol)

    for item in root.findall('item'):
        id = item.get('id')
        playtime = []
        for x in item.iter('*'):
            if(x.tag == 'item'):
                expdata[id] = {}
            if((x.tag == 'name')):
                #print('name yes')
                if('name' in lol):
                    if(x.get('type') == 'primary'):
                        expdata[id]['Name'] = x.get('value')
            if((x.tag == 'yearpublished')):
                #print('year yes')
                if('year' in lol):
                    expdata[id]['Year'] = x.get('value')
            if((x.tag == 'minplaytime')):
                #print('min time yes')
                if('playtime' in lol):
                    playtime.append(x.get('value'))
            if((x.tag == 'maxplaytime')):
                #print('max time yes')
                if('playtime' in lol):
                    playtime.append(x.get('value'))
            if((x.tag == 'minplayers')):
                #print('min play yes')
                if('players' in lol):
                    expdata[id]['Min. Players'] = x.get('value')
            if((x.tag == 'maxplayers')):
                #print('max play yes')
                if('players' in lol):
                    expdata[id]['Max Players'] = x.get('value')
            if('id' in lol):
                #print('id yes')
                if('id' in lol):
                    expdata[id]['UID'] = id
            if((x.tag == 'description')):
                #print('desc yes')
                if('description' in lol):
                    expdata[id]['Description'] = x.get('value')
            if('link' in lol):
                #print('link yes')
                if('link' in lol):
                    expdata[id]['Link'] = "https://boardgamegeek.com/boardgame/{}".format(id)
            if((x.tag == 'minage')):
                #print('age yes')
                if('age' in lol):
                    expdata[id]['Age'] = x.get('value')
            if( (x.tag == 'rank')):
                #print('bgg rank yes')
                if('bgg_rank' in lol):
                    if(x.get('friendlyname' == 'Board Game Rank')):
                        expdata[id]['BGG Rank'] = x.get('value')
            if((x.tag == 'usersrated')):
                #print('ratings c yes')
                if('ratings_c' in lol):
                    expdata[id]['# of Ratings'] = x.get('value')
            if( (x.tag == 'average')):
                #print('rating yes')
                if('rating' in lol):
                    expdata[id]['BGG Score'] = x.get('value')
            if((x.tag == 'averageweight')):
                #print('weight yes')
                if('complexity' in lol):
                    expdata[id]['Complexity'] = x.get('value')

            if(len(playtime) == 2):
                time = '-'.join(map(str,playtime))
                time = time + " min"
                expdata[id]['Playtime'] = time

    print(expdata)

#def dataGrab()
