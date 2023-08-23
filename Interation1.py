import urllib.request
from urllib.parse import urljoin
from html.parser import HTMLParser

# Define a custom HTML parser to extract links
class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (attr, value) in attrs:
                if attr == "href":
                    # Make the URL absolute by joining it with the base URL
                    absolute_url = urljoin(self.base_url, value)

                    # If the URL is not on the same domain, skip it
                    if "example.com" not in absolute_url:
                        continue

                    # Add the absolute URL to the set of links
                    self.links.add(absolute_url)

# Set the URL to start crawling from
url = "https://www.example.com/"

# Set the list of URLs to crawl
urls_to_crawl = [url]

# Set the set of visited URLs
visited_urls = set()

# Loop through the list of URLs to crawl
while urls_to_crawl:
    # Get the next URL to crawl
    url = urls_to_crawl.pop(0)

    # If we have already visited this URL, skip it
    if url in visited_urls:
        continue

    # Print the current URL being visited
    print("Visiting:", url)

    # Send the request and get the response
    response = urllib.request.urlopen(url)

    # Check if the content type is HTML
    content_type = response.getheader("Content-Type")
    if "text/html" not in content_type:
        continue

    # Parse the HTML content using our custom parser
    parser = LinkParser(url)
    parser.feed(response.read().decode())

    # Add the current URL to the set of visited URLs
    visited_urls.add(url)

    # Add the new URLs to the list of URLs to crawl
    urls_to_crawl.extend(parser.links)
