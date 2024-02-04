import requests
import yaml
import urllib
import webbrowser



def authentication():
    with open('secrets/secrets.yml', 'r') as file:
        secrets = yaml.safe_load(file)
        clintid = secrets['ClientID']
    #response = requests.get('https://www.strava.com/api/v3/athlete/', headers={'Authorization': 'Bearer ef41e29e0c140fdbc0675644013306a77755e2ba'})
    hello = urllib.request.urlopen('http://www.strava.com/oauth/authorize?client_id=90219&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read')
    hello1 = webbrowser.open('http://www.strava.com/oauth/authorize?client_id=90219&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read')
    #response = requests.get('http://www.strava.com/oauth/authorize?client_id=90219&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read')
    print(hello1)


# curl -X POST https://www.strava.com/oauth/token \
# 	-F client_id=YOURCLIENTID \
# 	-F client_secret=YOURCLIENTSECRET \
# 	-F code=AUTHORIZATIONCODE \
# 	-F grant_type=authorization_code

requests.post('https://www.strava.com/oauth/token',)