import requests
from bs4 import BeautifulSoup

def scrape_blog_titles(url):
    # Make an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and print the titles of articles
        titles = soup.find_all('a', class_='biglink')
        for title in titles:
            print(title.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example usage with a hypothetical blog site
    blog_url = "https://docs.python.org/3/"
    scrape_blog_titles(blog_url)
