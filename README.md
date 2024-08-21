# Openperplex

Openperplex is a powerful Python library for interacting with the Openperplex API, providing easy access to advanced search and content retrieval functionalities.
This library is in Alpha stage and is subject to change.
## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
   - [Initialization](#initialization)
   - [Search](#search)
   - [Simple Search](#simple-search)
   - [Streaming Search](#streaming-search)
   - [Website Content Retrieval](#website-content-retrieval)
   - [URL-based Querying](#url-based-querying)
4. [Parameter Specifications](#parameter-specifications)
   - [Response Language](#response-language)
   - [Location](#location)
5. [Error Handling](#error-handling)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

Install Openperplex using pip:

```bash
pip install --upgrade openperplex
```

## Getting Started

To use Openperplex, you'll need an API key. If you don't have one, create an account on the [Openperplex API website](https://api.openperplex.com) and get your API key from your account. 
The Api is free to use for 500 requests per month.

## Usage

### Initialization

First, import the Openperplex class and create an instance:

```python
from openperplex import Openperplex

api_key = "your_api_key_here"
client = Openperplex(api_key)
```

### Search

Perform a full search with sources, citations, and relevant questions:

```python
result = client.search(
    query="What are the latest developments in AI?",
    date_context="2023",
    location="us",
    pro_mode=True,
    response_language="en"
)

print(result["llm_response"])
print("Sources:", result["sources"])
print("Relevant Questions:", result["relevant_questions"])
```

### Simple Search

Perform a simple search that returns only the answer:

```python
answer = client.search_simple(
    query="Who won the FIFA World Cup in 2022?",
    location="fr",
    date_context="2023",
    pro_mode=False,
    response_language="fr"
)

print(answer)
```

### Streaming Search

Get search results in a stream, useful for displaying real-time updates:

```python
for chunk in client.search_stream(
    query="Explain quantum computing",
    date_context="2023",
    location="de",
    pro_mode=True,
    response_language="de"
):
    if chunk["type"] == "llm":
        print(chunk["text"], end="", flush=True)
    elif chunk["type"] == "sources":
        print("\nSources:", chunk["data"])
    elif chunk["type"] == "relevant_questions":
        print("\nRelevant Questions:", chunk["data"])
```

For a simpler streaming search:

```python
for chunk in client.search_simple_stream(
    query="What are the benefits of meditation?",
    location="es",
    date_context="2023",
    pro_mode=False,
    response_language="es"
):
    if chunk["type"] == "llm":
        print(chunk["text"], end="", flush=True)
```

### Website Content Retrieval

Retrieve text content from a website:

```python
text_content = client.get_website_text("https://www.example.com")
print(text_content)
```

Get a screenshot of a website:

```python
screenshot_url = client.get_website_screenshot("https://www.example.com")
print(f"Screenshot available at: {screenshot_url}")
```

Retrieve markdown content from a website:

```python
markdown_content = client.get_website_markdown("https://www.example.com")
print(markdown_content)
```

### URL-based Querying

Query content from a specific URL:

```python
response = client.query_from_url(
    url="https://www.example.com/article",
    query="What is the main topic of this article?",
    response_language="it"
)
print(response)
```

## Parameter Specifications

### Response Language

The `response_language` parameter allows you to specify the language of the API's response. Available options are:

- `"en"`: English
- `"es"`: Spanish
- `"it"`: Italian
- `"fr"`: French
- `"de"`: German (Allemand)
- `"auto"`: Automatically detect the language of the user's question

Example:
```python
result = client.search("Qual è la capitale dell'Italia?", response_language="it")
```

### Location

The `location` parameter helps provide more relevant results based on the country where the search is performed. Some available options include:

- `"us"`: United States
- `"fr"`: France
- `"es"`: Spain
- `"mx"`: Mexico
- `"ma"`: Morocco
- `"ca"`: Canada

Example:
```python
result = client.search("Meilleurs restaurants près de chez moi", location="fr", response_language="fr")
```

Using the appropriate `location` parameter can significantly improve the relevance of search results for location-specific queries.

## Error Handling

Openperplex uses custom exceptions for error handling. Always wrap your API calls in try-except blocks:

```python
from openperplex import Openperplex, OpenperplexError

client = Openperplex("your_api_key_here")

try:
    result = client.search("What is the meaning of life?")
    print(result)
except OpenperplexError as e:
    print(f"An error occurred: {e.status_code} - {e.detail}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
```

## Contributing

We welcome contributions! Please contact me on [Twitter](https://x.com/KhazzanYassine)

## License

Openperplex is released under the MIT License.