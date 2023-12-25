import requests
import json

class AgentLeader():
    def __init__(self,api_key,secret_key) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.dia_analyizer = 


class AiAgent():
    def __init__(self,api_key,secret_key) -> None:

        self.access_token = self.get_access_token(api_key,secret_key)
    
    def get_access_token(self,api_key,secret_key):
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")