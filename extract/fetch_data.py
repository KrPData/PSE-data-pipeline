import pandas as pd
import requests

class FetchData:

    def __init__(self, proxies, link):
        self.proxies = proxies
        self.link = link

    
    def get_data(self):
        response = requests.get(self.link,
                  proxies=self.proxies).json()
        return response
    
    def get_data_entsoe(self):
        response = requests.get(self.link,
            proxies=self.proxies)
        json_res = response.json()
        return json_res
    
    