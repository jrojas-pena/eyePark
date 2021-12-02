import requests

class http_eyepark_client():

    def __init__(self, config):
        self.config = config


    def checkPlateNumber(self, data):
        url = '%s:%d%s%d/%s/' % (self.config["server_url"], self.config["server_port"], self.config["check_plate_path"], data['parking-lot-number'], data['license-plate'])
        r = requests.get(url)
        return r.status_code == 200

    def addPlateNumber(self, data):
        url = self.config["server_url"]  + ':%d' % self.config["server_port"] + self.config["add_plate_path"]
        r = requests.post(json=data, url=url)
        return r.status_code == 200
    
    def alertSecurity(self):
        url = None
        r = requests.get(url)
        return r.status_code == 200
    
    def securityConfirmation(self):
        url = None
        r = requests.get(url)
        return r.status_code == 200

