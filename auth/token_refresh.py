#!/usr/bin/env python3

# to get new access token using refresh token
def refresh_access_token(client_id, client_secret, refresh_token):
    token_url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        new_refresh_token = token_data.get('refresh_token', refresh_token)
        # Do something with the new access token and refresh token, such as updating them in your database
        return access_token, new_refresh_token
    else:
        print(f"Error refreshing access token: {response.text}")
        return None, None

# Example usage
client_id = 'your_client_id'
client_secret = 'your_client_secret'
refresh_token = 'your_refresh_token'

new_access_token, new_refresh_token = refresh_access_token(client_id, client_secret, refresh_token)
if new_access_token:
    print(f"New access token: {new_access_token}")
    print(f"New refresh token: {new_refresh_token}")



# to check if a token has expired
import time

def is_token_expired(expires_at):
    current_time = time.time()
    return current_time >= expires_at

# Example usage:
expires_at = 1630387200  # Example value for expires_at (Unix timestamp)
is_expired = is_token_expired(expires_at)

if is_expired:
    print("Token has expired.")
else:
    print("Token is still valid.")
