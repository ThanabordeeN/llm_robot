import requests

class AI_Robot:
    def __init__(self):
        self.api_key = '8od9Jj2Gj34I9WwZaoECD9k4MR92IKvF'
    def generate_sound(self, text):
        url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
        headers = {'Apikey':self.api_key,'Content-Type' : 'application/json'}
        text = text
        data = {'input_text':text,'speaker':0 , 'phrase_break':1, 'audiovisual':0}
        response = requests.post(url, json=data, headers=headers)
        resp = requests.get(response.json()['wav_url'],headers={'Apikey':self.api_key})
        if resp.status_code == 200:
            with open('AI.wav', 'wb') as a:
                a.write(resp.content)
        else:
            print(resp.reason)
            
        
# Usage example:
