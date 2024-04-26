#!/usr/bin/env python3

import sys
from flask import Flask, request, redirect, Blueprint, render_template
import requests
import yaml
from database import getstrava_data

CLIENT_ID = '90219'
CLIENT_SECRET = 'e3a4f68ebd6db0d5754fb993f4f39abaa3878090'
STRAVA_AUTH_URL = 'http://www.strava.com/oauth/authorize'
REDIRECT_URI = 'http://127.0.0.1:5000/strava-auth/exchange-token'


auth = Blueprint('auth', __name__, url_prefix='/strava-auth', template_folder='templates')

@auth.route('/')
def index():
    # Redirect users to the Strava authorization URL
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'approval_prompt': 'force',
        'scope': 'read,activity:read'
    }
    strava_oauth_url = '{}?{}'.format(STRAVA_AUTH_URL, '&'.join([f'{k}={v}' for k, v in auth_params.items()]))
    return render_template('login.html', strava_oauth_url=strava_oauth_url)
    #return redirect(auth_url)


@auth.route('/exchange-token', methods=['GET']) # type: ignore
def exchange_token():
    # Exchange authorization code for access token
    code = request.args.get('code')
    token_params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    getstrava_data.get_access_token(token_params)
