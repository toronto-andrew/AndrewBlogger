from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

def create_service():
    # The file client_secret.json should be in the same directory as this script.
    # You can download this file from your Google Cloud Console.
    client_secrets_file = os.path.join(os.path.dirname(__file__), 'client_secret_393576596318-lrn16oinf4kq0g57a410p31ncl5rlvaf.apps.googleusercontent.com.json')

    # The scope for the OAuth2 request.
    scopes = ['https://www.googleapis.com/auth/blogger']

    # Create the flow using the client secrets file from the Google API Console.
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes=scopes)

    # Run the OAuth2 authorization flow. 'launch_browser' automatically opens a new browser tab
    # where you can complete the authentication process.
    credentials = flow.run_local_server(port=0)

    # Build the service object for the Blogger API.
    service = build('blogger', 'v3', credentials=credentials)
    return service

def list_blogs(service):
    # Get the list of blogs for the authenticated user.
    user_info = service.users().get(userId='self').execute()
    blogs = user_info.get('blogs', [])
    for blog in blogs:
        print(f"Blog Name: {blog['name']}, Blog ID: {blog['id']}")

# Create the service and list the blogs
service = create_service()
list_blogs(service)
