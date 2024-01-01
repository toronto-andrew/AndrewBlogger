import os

def generate_index_html(current_dir):
    folder_links = {}

    # Loop through each sub-folder in the current directory
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                # Create a relative path to the HTML file
                relative_path = os.path.join(os.path.relpath(root, current_dir), file)
                # Group the HTML links by folder
                folder = os.path.relpath(root, current_dir)
                if folder not in folder_links:
                    folder_links[folder] = []
                folder_links[folder].append(f'<a href="{relative_path}">{file}</a><br>')

    # Create HTML content for each group
    grouped_links_html = ""
    for folder, links in folder_links.items():
        grouped_links_html += f"<h2>{folder}</h2>\n" + ''.join(links)

    # Create the index.html content
    index_html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Andrew Liu's Blogger</title>
    </head>
    <body>
        <h1>Andrew Liu's Blogger</h1>
        {grouped_links_html}
    </body>
    </html>
    """

    # Write the content to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html_content)

if __name__ == '__main__':
    current_directory = '.'  # Current directory
    generate_index_html(current_directory)
