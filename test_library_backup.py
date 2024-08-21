import time

from src.openperplex.openperplex import Openperplex, \
    OpenperplexError  # Assuming you've saved the previous code as search_api_client.py
import asyncio

# Replace these with your actual credentials and API URL
API_KEY = "6RyMxR9VfvofmSNCjlY5lJxuvVw7fGPk5jkHavdOg9Q"

BASE_URL = "http://localhost:8000"  # Adjust this to your local server's address

client = Openperplex(API_KEY, BASE_URL)


# test ok openai
def test_search():
    try:
        start_time = time.time()
        result = client.search("financial information natais group", response_language='en',pro_mode=True,location='fr')
        print("Search Result:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in search: {e}")


def test_search_stream():
    try:
        start_time = time.time()
        print("Search Stream Results:")
        for chunk in client.search_stream("Who won the last World Cup?", response_language='es', pro_mode=False):
            print(chunk)

        print(f"Time taken SEARCH STREAM : {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in search_stream: {e}")


# working error handling
def test_search_simple():
    try:
        start_time = time.time()
        result = client.search_simple("san francisco weather today", pro_mode=True, location='us',
                                      response_language='en')
        print("Simple Search Result:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in search_simple: {e}")


def test_search_simple_stream():
    try:
        start_time = time.time()
        print("Simple Search Stream Results:")
        for chunk in client.search_simple_stream("Who won the last World Cup? and with which score",
                                                 response_language='en', pro_mode=False):
            print(chunk)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in search_simple_stream: {e}")


def test_get_website_text():
    try:
        start_time = time.time()
        result = client.get_website_text("https://www.bbc.com/news/world")
        print("Website Text:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in get_website_text: {e}")


def test_get_website_screenshot():
    try:
        start_time = time.time()
        result = client.get_website_screenshot("https://www.bbc.com/news/world")
        print("Website screenshot:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in get_website_screenshot: {e}")


def test_get_website_markdown():
    try:
        start_time = time.time()
        result = client.get_website_markdown("https://www.bbc.com/news/world")
        print("Website markdown:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in get_website_markdown: {e}")


def test_query_from_url():
    try:
        start_time = time.time()
        result = client.query_from_url("https://www.paulgraham.com/users.html",
                                       "explain this article, what is it about?")
        print("Website query url:")
        print(result)
        print(f"Time taken: {time.time() - start_time}")
    except OpenperplexError as e:
        print(f"ERROR in test_query_from_url: {e}")


if __name__ == "__main__":
    #test_search()
    #test_search_stream()
    #test_search_simple()
    #test_search_simple_stream()
    #test_get_website_text()
    #test_get_website_screenshot()
    #test_get_website_markdown()
    test_query_from_url()
