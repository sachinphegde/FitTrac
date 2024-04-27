#!/usr/bin/env python3
'''To get data from Strava and put in database'''
import datetime
import requests
from database import database

TOKEN_EXCHANGE_URL = 'https://www.strava.com/oauth/token'
BASE_URL = "https://www.strava.com/api/v3"
DATABASE_PATH = 'database/fitTrac'


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

athlete_data_to_store = {'id': 'string',
                'username': 'string',
                'firstname': 'string', 
                'lastname': 'string', 
                'sex': 'string', 
                'weight': 'string', 
                'city': 'string', 
                'access_token': 'string', 
                'refresh_token': 'string', 
                'expires_at': 'string'}

def add_user_data(data):
    '''gets the access token for the new logged in user'''
    database.create_table(DATABASE_PATH, 'athleteInfo', athlete_data_to_store)
    athlete_data = [data['athlete']['id'],
                    data['athlete']['username'],
                    data['athlete']['firstname'],
                    data['athlete']['lastname'],
                    data['athlete']['sex'],
                    data['athlete']['weight'],
                    data['athlete']['city'],
                    data['access_token'],
                    data['refresh_token'],
                    data['expires_at']]
    database.insert_data(DATABASE_PATH, 'athleteInfo', 'id', data['athlete']['id'], athlete_data)

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
