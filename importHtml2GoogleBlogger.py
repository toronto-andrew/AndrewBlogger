from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Authenticate and create the service
def create_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret_393576596318-lrn16oinf4kq0g57a410p31ncl5rlvaf.apps.googleusercontent.com.json',
        scopes=['https://www.googleapis.com/auth/blogger']
    )
    credentials = flow.run_local_server(port=0)
    return build('blogger', 'v3', credentials=credentials)

def create_post(service, blog_id, html_content, title):
    body = {
        'title': title,
        'content': html_content
    }
    posts = service.posts()
    posts.insert(blogId=blog_id, body=body, isDraft=False).execute()

# Main function
def upload_html_to_blogger(blog_id, folder_path):
    service = create_service()
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                html_content = file.read()
                title = filename.replace('.html', '')
                create_post(service, blog_id, html_content, title)

if __name__ == '__main__':
    my_blog_id = '8643292085161037833' # Replace with your Blogger blog ID
    folder_path = '/home/andrew/PycharmProjects/updateHtml4Images/玛雅史记' # Replace with the path to your HTML files
    upload_html_to_blogger(my_blog_id, folder_path)
