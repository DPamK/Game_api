import requests
import json

class AgentLeader():
    def __init__(self,api_key,secret_key) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.dia_analyizer = 


class Agent():
    def __init__(self,client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.get_access_token()
    
    def get_access_token(self):
        url = 'https://example.com/oauth/token'
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json()['access_token']
    

class QianfanAgent(Agent):
    def __init__(self, client_id, client_secret,api_url) -> None:
        super().__init__(client_id, client_secret)
        self.api_url = api_url
    
    def get_access_token(self):
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}"
    
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    def request_api(self,msg):
        payload = json.dumps(msg)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST",self.api_url, headers=headers, data=payload)
        return response

