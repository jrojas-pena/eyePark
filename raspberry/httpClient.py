import httpx
import json


def checkPlateNumber(data, config):
    with httpx.Client() as client:
        url = '%s:%d%s%d/%s/' % (config["server_url"], config["server_port"], config["check_plate_path"], data['parking-lot-number'], data['license-plate'])
        r = client.get(url)
        return r.status_code == 200

def addPlateNumber(data, config):
    with httpx.Client() as client:
        url = config["server_url"]  + ':%d' % config["server_port"] + config["add_plate_path"]
        r = client.post(json=data, url=url)
        return r.status_code == 200

