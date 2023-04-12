import requests

from pprint import pprint
heroes_list = ['Hulk', 'Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
url = 'https://akabab.github.io/superhero-api/api/all.json'


hero_dict = requests.get(url).json()
for hero in hero_dict:
    if hero['name'] in intelligence_dict:
        intelligence_dict[hero['name']]=hero["powerstats"]["intelligence"]
        
for hero in intelligence_dict:
    if max(intelligence_dict.values())==intelligence_dict[hero]:
        print(hero)