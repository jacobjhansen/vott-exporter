import json

class Asset:

    def __init__(self,identifier,source,timestamp):
        self.identifier = identifier
        self.source = source
        self.timestamp = timestamp
        self.region_list = []

    def add_region(self,region):
        self.region_list.append(region)

class Region:

    def __init__(self,identifier,shape,tag,x,y,width,height):
        self.identifier = identifier
        self.shape = shape
        self.tag = tag
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def returnJSONAssetName(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data['asset']['name'].split('#')[0]

def return_asset(file_path,raw_videos):
    with open(file_path) as f:
        data = json.load(f)
    identifier = data['asset']['id']
    source = [x for x in raw_videos if x.endswith(data['asset']['parent']['name'])][0]
    timestamp = data['asset']['timestamp']

    current_asset = Asset(identifier,source,timestamp)
    
    for region in data['regions']:
        region_id = region['id']
        region_shape = region['type']
        region_tag = region['tags'][0]
        region_x = region['boundingBox']['left']
        region_y = region['boundingBox']['top']
        region_width = region['boundingBox']['width']
        region_height = region['boundingBox']['height']

        current_region = Region(region_id,region_shape,region_tag,region_x,region_y,region_width,region_height)

        current_asset.add_region(current_region)

    return current_asset

def return_asset_list(raw_objects,raw_videos):
    asset_list = []

    for item in raw_objects:
        try:
            asset_list.append(return_asset(item,raw_videos))
        except:
            pass

    return asset_list
