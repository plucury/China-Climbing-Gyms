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
    with open('gyms.json', 'w') as f:
        json.dump(gyms, f, indent=4)
