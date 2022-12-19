import json
import re
from mapbox import Geocoder

MAPBOX_ACCESS_TOKEN = ''  # вставляй свой


def get_coords(address: str) -> list[float]:
    geocoder = Geocoder(access_token=MAPBOX_ACCESS_TOKEN)
    response = geocoder.forward(address)
    try:
        coords = str(response.json()['features'][0]['center'])
        coords = list(map(float, coords[1:-1].replace(',', ' ').split()))
        coords[0], coords[1] = coords[1], coords[0]
        return coords
    except:
        return [None, None]


with open("/Users/free001style/free001style/Cian/Cian_flats.json", encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

for offer in data:
    offer["name"] = offer["name"].replace("\xa0", " ")
    offer["price"] = offer["price"].replace("\xa0", "")[:-1]
    offer["price"] = re.sub(r"\D+", "", offer["price"])
    if offer["price"] != '':
        offer["price"] = int(offer["price"])
    offer["available_metro_station"] = re.sub(re.compile(r'(от )*\d{2}(–*)(\d{2})*( мин.)*'), ' ',
                                              offer["available_metro_station"]).split()
    offer["total_information"] = offer["total_information"].replace("\xa0", " ")
    offer["address"] = re.sub(re.compile(r'(?<=\w)([А-Я])'), r' \1', offer["address"])
    offer["address"] = re.sub(re.compile(r'(\d+(\.\d+)?)'), r' \1', offer["address"])
    offer["coords"] = get_coords(offer["address"])
    offer["photos"] = offer["photos"][:offer["photos"].find('jpg') + 3]

with open("/Users/free001style/free001style/Cian/Cian_flats.json", encoding='utf-8', errors='ignore',
          mode='w') as file:
    json.dump(data, file, ensure_ascii=False)
