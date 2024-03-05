#!/usr/bin/env python3

import sys
from flask import Flask, request, redirect, Blueprint
import requests
import yaml
import datetime
from database import getstrava_data


auth = Blueprint('main', __name__, url_prefix='/home')

@auth.route('/')
def index():
    

@auth.route('/data')
def data():
    return f'hello'