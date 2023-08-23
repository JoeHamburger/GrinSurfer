import urllib.request

# Set the URL to download
url = "https://scp-wiki.wikidot.com/"

# Send the request and get the response
response = urllib.request.urlopen(url)

# Check if the content type is HTML
content_type = response.getheader("Content-Type")
if "text/html" not in content_type:
    print("Error: the URL does not contain HTML content")
    exit()

# Read the HTML content and print it
html_content = response.read().decode()
print(html_content)
