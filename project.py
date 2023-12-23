# import the necessary libraries
import requests
from bs4 import BeautifulSoup

# define a function to crawl data from a URL
def crawl_data(url):
    # retrieve HTML data from the URL
    response = requests.get(url)
    html = response.text

    # use BeautifulSoup to extract data from HTML
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.body.text.strip()

    # return the extracted data
    return {
        'title': title,
        'body': body
    }
