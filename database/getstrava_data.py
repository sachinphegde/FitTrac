#!/usr/bin/env python3
'''To get data from Strava and put in database'''
import datetime
import requests
from database import database

TOKEN_EXCHANGE_URL = 'https://www.strava.com/oauth/token'
BASE_URL = "https://www.strava.com/api/v3"


def get_activities(access_token):
    '''get the activities of the athlete'''
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{BASE_URL}/athlete/activities", headers=headers, timeout=50)
    if response.status_code == 200:
        activities = response.json()
        for activity in activities:
            print(activity)
    else:
        print(f"Error: {response.status_code}, {response.text}")


def add_user_data(data):
    '''gets the access token for the new logged in user'''
    database.create_table('fitTrac', 'userData', {'id': 'string', 'username': 'string'})
    database.insert_data('fitTrac', 'userData', [data['athlete']['id'], data['athlete']['username']])
    database.add_new_row_if_not_exists('fitTrac', 'userData', 'id', data['athlete']['id'], [data['athlete']['id'], data['athlete']['username']])

def get_access_token(token_params):
    '''gets the access token for the new logged in user'''
    response = requests.post(TOKEN_EXCHANGE_URL, data=token_params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        # check if the user is present
        add_user_data(data)
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        print(f"Access token: {access_token}")
        print(f"Refresh token: {refresh_token}")
        print(data)
    else:
        print(f"Error getting access token: {response.text}")

def get_utc_time():
    expires_at_unix_timestamp = response.json().get('expires_at')
    expires_at_datetime = datetime.datetime.utcfromtimestamp(expires_at_unix_timestamp)
    print("Expires at:", expires_at_datetime)
