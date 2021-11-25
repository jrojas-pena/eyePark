import requests

class http_eyepark_client(requests):

    def __init__(self, config):
        super().__init__()
        self.config = config

    def checkPlateNumber(self, data):
        url = '%s:%d%s%d/%s/' % (self.config["server_url"], self.config["server_port"], self.config["check_plate_path"], data['parking-lot-number'], data['license-plate'])
        r = self.get(url)
        return r.status_code == 200

    def addPlateNumber(self, data):
        url = self.config["server_url"]  + ':%d' % self.config["server_port"] + self.config["add_plate_path"]
        r = self.post(json=data, url=url)
        return r.status_code == 200

