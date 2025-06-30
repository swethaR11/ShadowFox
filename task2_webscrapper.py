#Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy.
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status
        return response.text
    except requests.RequestException as e:
        print("Error fetching the webpage:", e)
        return None

def extract_quotes(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        quotes_data.append((text, author))

    return quotes_data

def display_quotes(quotes_data):
    for i, (quote, author) in enumerate(quotes_data, 1):
        print(f"{i}. {quote} — {author}")

# Main program
url = "http://quotes.toscrape.com"
html_content = fetch_html(url)

if html_content:
    quotes = extract_quotes(html_content)
    display_quotes(quotes)
