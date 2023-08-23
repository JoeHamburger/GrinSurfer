import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

# define the starting URL
url = "https://scp-wiki.wikidot.com/"

# create a set to store visited URLs
visited_urls = set()

# create a list to store URLs to visit
urls_to_visit = [url]

# create a subclass of HTMLParser to find links in HTML
class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    # join the URL with the base URL to handle relative links
                    absolute_url = urljoin(url, attr[1])
                    # if the URL is not already visited or in the list of URLs to visit, add it to the list
                    if absolute_url not in visited_urls and absolute_url not in urls_to_visit:
                        urls_to_visit.append(absolute_url)

# loop through the URLs to visit
while urls_to_visit:
    # pop the next URL to visit from the list
    url = urls_to_visit.pop(0)
    
    # if the URL has already been visited, skip it
    if url in visited_urls:
        continue
    
    # fetch the contents of the URL
    with urllib.request.urlopen(url) as response:
        content = response.read()
    
    # parse the HTML to find links to other pages on the website
    parser = LinkParser()
    parser.feed(content.decode())
    
    # add the current URL to the set of visited URLs
    visited_urls.add(url)
    
    # do something with the contents of the URL
    print(f"Fetched {url} ({len(content)} bytes)")
