import requests
import pandas as pd

#reporting_codes = _get_reporting_codes()
#partner_codes = _get_partner_codes()
#trade_flow_codes = {"import" : 1, "export" : 2,
#                    "re-export" : 3, "re-import" : 4,
#                    "all" : "all"}


class uncomtrade:
    
    def __init__(self, apikey, params):
        self.Baseurl = "http://comtrade.un.org/api/"
        self.apikey = apikey
        self.params = params
        
        self.get_params()
        
    def get_params(self):
        for key, value in self.params.items():
            self.params_string += "&" + key + "=" + value
        return self.params_string
    
    def make_request(self, http_method="GET"):
        url = self.Baseurl + "get?" + self.params_string
        payload={}
        headers = {}
        response = requests.request(http_method, url, headers=headers, data=payload)
        return response.text
    
    def save_data(self):
        
        pass
        
def main():
    url = "http://comtrade.un.org/api/get?max=502&type=S&freq=A&px=EB02&ps=2020&r=4&p=all&rg=1&cc=ALL"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    pass

def get_data():
    # Escoger los parametros que son dinamicos
    PARAMS = [
        {"ps" : "2020"},
        {"ps" : "2019"},
        {"ps" : "2018"},
    ]

    for param in PARAMS:
        # Hacer la peticion
        # Guardar los datos en un archivo

    
    pass

if __name__ == "__main__":
    main()