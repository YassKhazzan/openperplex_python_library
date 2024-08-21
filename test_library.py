import time

# Assuming you've saved the previous code as search_api_client.py
import asyncio

# Replace these with your actual credentials and API URL
# API_KEY = "6RyMxR9VfvofmSNCjlY5lJxuvVw7fGPk5jkHavdOg9Q"

from openperplex import Openperplex, OpenperplexError

# initialize the client
client = Openperplex(API_KEY)


# Perform a search and get the response with sources and citations
def search():
    try:
        result = client.search("NVIDIA's financial data",
                               response_language='en',
                               pro_mode=True,
                               location='us')
        print(result)
    except OpenperplexError as e:
        print(f"ERROR in search: {e}")


# Perform a search and get the response in a stream
def search_stream():
    try:
        for chunk in client.search_stream("Who won the last World Cup?",
                                          response_language='es',
                                          pro_mode=False):
            print(chunk)
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
