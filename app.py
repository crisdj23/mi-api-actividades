```py file="api_client.py"
[v0-no-op-code-block-prefix]import requests
import json

BASE_URL = "https://tu-url-de-render.onrender.com"

def get_activities():
    """
    Retrieves all activities from the API.
    """
    url = f"{BASE_URL}/activities"
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    return response.json()

def create_activity(activity_data):
    """
    Creates a new activity via the API.
    """
    url = f"{BASE_URL}/activities"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(activity_data)
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    # Example Usage (replace with your actual data and URL)
    # You'll need a Render deployment to test this properly.

    # Get activities
    try:
        activities = get_activities()
        print("Activities:", activities)
    except requests.exceptions.RequestException as e:
        print(f"Error getting activities: {e}")

    # Create a new activity
    new_activity = {
        "title": "Example Activity",
        "description": "This is an example activity created via the API.",
        "due_date": "2024-12-31"
    }

    try:
        created_activity = create_activity(new_activity)
        print("Created Activity:", created_activity)
    except requests.exceptions.RequestException as e:
        print(f"Error creating activity: {e}")

