#!/usr/bin/env python3
'''refresh the access token'''

import time
import requests

def refresh_access_token(client_id, client_secret, refresh_token):
    '''Method to get new access token using refresh token'''
    token_url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    response = requests.post(token_url, data=payload, timeout=60)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        new_refresh_token = token_data.get('refresh_token', refresh_token)
        return access_token, new_refresh_token
    else:
        print(f"Error refreshing access token: {response.text}")
        return None, None


def is_token_expired(expires_at):
    '''Method to check if token has expired'''
    current_time = time.time()
    is_expired = current_time >= expires_at
    if is_expired:
        print("Token has expired.")
    else:
        print("Token is still valid.")
