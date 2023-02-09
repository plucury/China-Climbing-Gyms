import json
import os
import yaml


if __name__ == '__main__':
    gyms = []
    for path, _, files in os.walk('gyms'):
        for file in files:
            with open(os.path.join(path, file), 'r') as f:
                r = yaml.safe_load(f)
                gyms.append(r)
    city_dict = {}
    last_city = None
    for gym in gyms:
        city = gym['city']
        if city not in city_dict:
            city_dict[city] = {}
            city_dict[city]['gyms'] = []
            city_dict[city]['city'] = city
            city_dict[city]['province'] = gym['province']
        city_dict[city]['gyms'].append(gym)
    citys = sorted(city_dict.values(),
                   key=lambda x: x['province']+":"+x['city'])
    for city in citys:
        city['gyms'].sort(key=lambda x: x['name'])

    with open('gyms.json', 'w') as f:
        json.dump(citys, f, indent=4)
