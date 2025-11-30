class Proxy_config:

    def __init__(self):
        self.http_proxy = ""
        self.https_proxy = ""

    def get_proxies(self) -> dict: 
        return {
            "http": self.http_proxy,
            "https": self.https_proxy
        }