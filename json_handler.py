import json

def returnJSON(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data['asset']['name'].split('#')[0]