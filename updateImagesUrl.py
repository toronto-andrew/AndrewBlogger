# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def download_image(url, folder):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Extract the filename from the URL
    filename = os.path.basename(urlparse(url).path)
    local_filename = os.path.join(folder, filename)

    # Download and save the image
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename


def update_html(html_file, output_folder):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for img in soup.find_all('img'):
        image_url = img['src']
        downloaded_image = download_image(image_url, output_folder)
        img['src'] = downloaded_image

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))


def process_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            html_file_path = os.path.join(folder_path, filename)
            update_html(html_file_path, output_folder)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_folder = '/home/andrew/PycharmProjects/updateHtml4Images/玛雅史记'
    output_folder = '/home/andrew/PycharmProjects/updateHtml4Images/玛雅史记'
    process_folder(input_folder, output_folder)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
