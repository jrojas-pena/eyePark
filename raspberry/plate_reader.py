from openalpr import Alpr
from argparse import ArgumentParser


class plate_reader:

    def __init__(self, country, config_file, runtime_data):
        self.alpr = None        
        try:
            self.alpr = Alpr(country, config_file, runtime_data)
            self.alpr.set_top_n(1)
        except:
            self.close()
    
    def close(self):
        if self.alpr:
            self.alpr.unload()

    def read_plate(self, image):
        jpeg_bytes = open(image, "rb").read()
        results = self.alpr.recognize_array(jpeg_bytes)
        print(results['results'][0]['plate'])
    
    def __enter__(self):
        return self
    
    def __exit__(self):
        self.close()
    
    def __del__(self):
        self.close()





