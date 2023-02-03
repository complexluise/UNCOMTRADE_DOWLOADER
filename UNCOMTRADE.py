import requests
import pandas as pd
import json
import logging

LOG = logging.getLogger(__name__)

#reporting_codes = _get_reporting_codes()
#partner_codes = _get_partner_codes()
#trade_flow_codes = {"import" : 1, "export" : 2,
#                    "re-export" : 3, "re-import" : 4,
#                    "all" : "all"}



class uncomtrade:
    """
    This class makes requests to the UN Comtrade API.

    Attributes:
        Baseurl (str): The base URL for the UN Comtrade API.
        apikey (str): The API key for authentication.
        params (dict): The parameters for the API request.
        params_string (str): The string representation of the parameters for the API request.
    
    """

    def __init__(self, apikey, params):
        """
        The constructor for the `uncomtrade` class.

        Args:
            apikey (str): The API key for authentication.
            params (dict): The parameters for the API request.
        
        """
        self.Baseurl = "http://comtrade.un.org/api/"
        self.apikey = apikey
        
    def get_params(self, params):
        """
        This method creates the string representation of the parameters for the API request.

        Returns:
            str: The string representation of the parameters for the API request.
        
        """
        for key, value in params.items():
            self.params_string += "&" + key + "=" + value
        return self.params_string
    
    def make_request(self, http_method="GET"):
        """
        This method makes a request to the UN Comtrade API.

        Args:
            http_method (str, optional): The HTTP method to use for the request. Defaults to "GET".

        Returns:
            str: The text of the API response.
        
        """
        url = self.Baseurl + "get?" + self.params_string
        payload={}
        headers = {}
        response = requests.request(http_method, url, headers=headers, data=payload)
        return response.text
    
    def validate_response(self, response):
        pass
    
    def get_data(self):
        """
        This method gets the data from the API response.

        Returns:
            pandas.DataFrame: The data from the API response.
        
        """
        data = self.make_request()
        if self.
        data = pd.read_json(data)
        return data

    
    def save_data(self):
        
        pass
        
def main():
    url = "http://comtrade.un.org/api/get?max=502&type=S&freq=A&px=EB02&ps=2020&r=all&p=8&rg=2&cc=ALL"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())

def get_data():
    # Escoger los parametros que son dinamicos
    YEARS = [
        {"ps" : "2020"},
        {"ps" : "2019"},
        {"ps" : "2018"},
    ]
    
    TYPE_OPERATION = [{"rg" : "2"},
                      {"rg" : "1"}]
    
    PARTNER_CODES = [{"p" : "8"},
                     {"p" : "all"}]
    
    COMTRADE = uncomtrade("api_key")
    
    for YEAR in YEARS:
        for PAIS in PARTNER_CODES:
            for TIPO in TYPE_OPERATION:
    
                PARAMETROS = [{"max" : "502"},
                                    {"type" : "S"},
                                    {"freq" : "A"},
                                    {"px" : "EB02"},
                                    {"ps" : YEAR},
                                    {"r" : "all"},
                                    {"p" : PAIS},
                                    {"rg" : TIPO},
                                    {"cc" : "ALL"}]
                
                COMTRADE.get_params(PARAMETROS)
                COMTRADE.get_data()
                COMTRADE.save_data()


if __name__ == "__main__":
    main()