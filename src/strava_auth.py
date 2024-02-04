from flask import Flask, request, redirect
import requests
import yaml
import datetime



# def authentication():
#     with open('secrets/secrets.yml', 'r') as file:
#         secrets = yaml.safe_load(file)
#         clintid = secrets['ClientID']
#     #response = requests.get('https://www.strava.com/api/v3/athlete/', headers={'Authorization': 'Bearer ef41e29e0c140fdbc0675644013306a77755e2ba'})



app = Flask(__name__)

CLIENT_ID = '90219'
CLIENT_SECRET = 'e3a4f68ebd6db0d5754fb993f4f39abaa3878090'
STRAVA_AUTH_URL = 'http://www.strava.com/oauth/authorize'
TOKEN_EXCHANGE_URL = 'https://www.strava.com/oauth/token'
REDIRECT_URI = 'http://127.0.0.1:5000/exchange_token'

@app.route('/')
def index():
    # Redirect users to the Strava authorization URL
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'approval_prompt': 'force',
        'scope': 'read'
    }
    auth_url = '{}?{}'.format(STRAVA_AUTH_URL, '&'.join([f'{k}={v}' for k, v in auth_params.items()]))
    return redirect(auth_url)

@app.route('/exchange_token')
def exchange_token():
    # Exchange authorization code for access token
    code = request.args.get('code')
    token_params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    response = requests.post(TOKEN_EXCHANGE_URL, data=token_params)
    access_token = response.json().get('access_token')

    # Do something with the access token, like make API requests
    # For example:
    strava_data = requests.get('https://www.strava.com/api/v3/athlete', headers={'Authorization': f'Bearer {access_token}'}).json()


    expires_at_unix_timestamp = response.json().get('expires_at')
    expires_at_datetime = datetime.datetime.utcfromtimestamp(expires_at_unix_timestamp)
    #print("Expires at:", expires_at_datetime)


    return f'expiry date: {expires_at_datetime}, strava data: {strava_data}'

if __name__ == '__main__':
    app.run(debug=True)


# # to get new access token using refresh token
# def refresh_access_token(client_id, client_secret, refresh_token):
#     token_url = 'https://www.strava.com/oauth/token'
#     payload = {
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'refresh_token': refresh_token,
#         'grant_type': 'refresh_token'
#     }
#     response = requests.post(token_url, data=payload)
#     if response.status_code == 200:
#         token_data = response.json()
#         access_token = token_data['access_token']
#         new_refresh_token = token_data.get('refresh_token', refresh_token)
#         # Do something with the new access token and refresh token, such as updating them in your database
#         return access_token, new_refresh_token
#     else:
#         print(f"Error refreshing access token: {response.text}")
#         return None, None

# # Example usage
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'
# refresh_token = 'your_refresh_token'

# new_access_token, new_refresh_token = refresh_access_token(client_id, client_secret, refresh_token)
# if new_access_token:
#     print(f"New access token: {new_access_token}")
#     print(f"New refresh token: {new_refresh_token}")



# TODO: chek if we get the exchange token or not and based on that throw error or collect user data
# TODO:   storing the data in database
# TODO: gettin new access token using refresh token and doing it befoe it expires
# TODO: create an architecture for api's

