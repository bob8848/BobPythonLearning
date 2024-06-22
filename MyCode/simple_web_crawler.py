# simple_web_crawler.py
import requests
from bs4 import BeautifulSoup
import re

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for anchor in soup.find_all('a', href=True):
        link = anchor['href']
        if not re.match(r'^https?://', link):
            link = base_url + link
        links.add(link)
    return links

def crawl(start_url, depth):
    visited = set()
    to_visit = {start_url}
    while to_visit and depth > 0:
        next_to_visit = set()
        for url in to_visit:
            if url not in visited:
                visited.add(url)
                html = fetch_html(url)
                if html:
                    next_to_visit.update(parse_links(html, start_url))
        to_visit = next_to_visit
        depth -= 1
    return visited

if __name__ == "__main__":
    start_url = "https://example.com"
    depth = 2
    visited_links = crawl(start_url, depth)
    print("Visited links:")
    for link in visited_links:
        print(link)
