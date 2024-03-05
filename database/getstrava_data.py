import requests
 
# Get activities for the authenticated user
def get_activities(url, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{url}/athlete/activities", headers=headers)
    if response.status_code == 200:
        activities = response.json()
        for activity in activities:
            print(activity)
    else:
        print(f"Error: {response.status_code}, {response.text}")