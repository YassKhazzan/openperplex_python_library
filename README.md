# Openperplex Python Library Documentation

The Openperplex Python library provides an interface to interact with the Openperplex API, allowing you to perform various search and web-related operations.

## Installation

To install the Openperplex library, use pip:

```bash
pip install --upgrade openperplex
```

## Initialization

To use the Openperplex library, you need to initialize it with your API key:

```python
from openperplex import Openperplex

api_key = "your_openperplex_api_key_here"
client = Openperplex(api_key)
```

## Available Methods

### 1. search

Perform a non-streaming search query.

```python
result = client.search(
    query="What are the latest developments in AI?",
    date_context="2024-08-25",  # if empty, the current date of the api server is used
    location="us",  # default is "us"
    pro_mode=False,  # default is False
    response_language="en"  # default is "auto"
)

print(result["llm_response"])
print(result["images"])
print("Sources:", result["sources"])
print("Relevant Questions:", result["relevant_questions"])
```

### 2. search_simple

Perform a simplified non-streaming search query.

```python
answer = client.search_simple(
    query="Who won the FIFA World Cup in 2022?",
    location="fr",
    date_context="2024-08-25 7:00 AM",
    pro_mode=False,
    response_language="fr",
    answer_type="text"
)

print(answer["llm_response"])
```

### 3. search_stream

Perform a streaming search query.

```python
for chunk in client.search_stream(
    query="Explain quantum computing",
    date_context="2024-08-25 7:00 AM",
    location="de",
    pro_mode=False,
    response_language="de",
    answer_type="markdown"
):
    if chunk["type"] == "llm":
        print(chunk["text"], end="", flush=True)
    elif chunk["type"] == "sources":
        print("Sources:", chunk["data"])
    elif chunk["type"] == "relevant_questions":
        print("Relevant Questions:", chunk["data"])
```

Example with pro_mode enabled:

```python
for chunk in client.search_stream(
    query="Explain quantum computing",
    date_context="2024-08-25 7:00 AM",
    location="us",
    pro_mode=True,
    response_language="auto",
    answer_type="html"
):
    if chunk["type"] == "llm":
        print(chunk["text"], end="", flush=True)
```

### 4. get_website_text

Retrieve the text content of a website.

```python
result = client.get_website_text("https://www.example.com")
print(result)
```

### 5. get_website_markdown

Get the markdown representation of a website.

```python
result = client.get_website_markdown("https://www.example.com")
print(result)
```

### 6. get_website_screenshot

Get a screenshot of a website.

```python
result = client.get_website_screenshot("https://www.example.com")
print(f"Screenshot available at: {result['url']}")
```

### 7. query_from_url

Perform a query based on the content of a specific URL.

```python
response = client.query_from_url(
    url="https://www.example.com/article",
    query="What is the main topic of this article?",
    response_language="it",
    answer_type="text"  # default is "text" if not specified
)
print(response)
```

## Parameters

### query
The search query or question.

### date_context
Optional date for context (format: "YYYY-MM-DD" or "YYYY-MM-DD HH:MM AM/PM"). If empty, the current date of the API server is used.

### location
Country code for search context. Default is "us". See the list of supported locations below.

### pro_mode
Boolean to enable or disable pro mode. Default is False.

### response_language
Language code for the response. Default is "auto" (auto-detect). See the list of supported languages below.

### answer_type
Type of answer format. Options are "text" (default), "markdown", or "html".

## Supported Locations

The `location` parameter accepts the following country codes:

🇺🇸 us (United States), 🇨🇦 ca (Canada), 🇬🇧 uk (United Kingdom), 🇲🇽 mx (Mexico), 🇪🇸 es (Spain), 🇩🇪 de (Germany), 🇫🇷 fr (France), 🇵🇹 pt (Portugal), 🇳🇱 nl (Netherlands), 🇹🇷 tr (Turkey), 🇮🇹 it (Italy), 🇵🇱 pl (Poland), 🇷🇺 ru (Russia), 🇿🇦 za (South Africa), 🇦🇪 ae (United Arab Emirates), 🇸🇦 sa (Saudi Arabia), 🇦🇷 ar (Argentina), 🇧🇷 br (Brazil), 🇦🇺 au (Australia), 🇨🇳 cn (China), 🇰🇷 kr (Korea), 🇯🇵 jp (Japan), 🇮🇳 in (India), 🇵🇸 ps (Palestine), 🇰🇼 kw (Kuwait), 🇴🇲 om (Oman), 🇶🇦 qa (Qatar), 🇮🇱 il (Israel), 🇲🇦 ma (Morocco), 🇪🇬 eg (Egypt), 🇮🇷 ir (Iran), 🇱🇾 ly (Libya), 🇾🇪 ye (Yemen), 🇮🇩 id (Indonesia), 🇵🇰 pk (Pakistan), 🇧🇩 bd (Bangladesh), 🇲🇾 my (Malaysia), 🇵🇭 ph (Philippines), 🇹🇭 th (Thailand), 🇻🇳 vn (Vietnam)

## Supported Languages

The `response_language` parameter accepts the following language codes:

- `auto`: Auto-detect the user question language (default)
- `en`: English
- `fr`: French
- `es`: Spanish
- `de`: German
- `it`: Italian
- `pt`: Portuguese
- `nl`: Dutch
- `ja`: Japanese
- `ko`: Korean
- `zh`: Chinese
- `ar`: Arabic
- `ru`: Russian
- `tr`: Turkish
- `hi`: Hindi

## Response Structure

### search and search_simple methods
- `llm_response`: The main response from the language model.
- `images`: (if available) A list of relevant images.
- `sources`: A list of sources used to generate the response.
- `relevant_questions`: A list of related questions that might be of interest.

### search_stream method
The streaming response is divided into chunks, each with a `type` field:
- `llm`: Contains the `text` field with a part of the language model's response.
- `sources`: Contains the `data` field with a list of sources.
- `relevant_questions`: Contains the `data` field with a list of related questions.

### get_website_screenshot method
- `url`: The URL where the screenshot can be accessed.

## Error Handling

The library raises `OpenperplexError` exceptions for API errors. Always wrap your API calls in try-except blocks:

```python
from openperplex import Openperplex, OpenperplexError

try:
    result = client.search("AI advancements")
    print(result["llm_response"])
except OpenperplexError as e:
    print(f"An error occurred: {e}")
```

Remember to handle potential network errors and other exceptions as needed in your application.

## Best Practices

1. **API Key Security**: Never hard-code your API key in your source code. Use environment variables or secure configuration management.

2. **Error Handling**: Always implement proper error handling to manage API errors and network issues gracefully.

3. **Rate Limiting**: Be aware of any rate limits imposed by the Openperplex API and implement appropriate backoff strategies if necessary.

4. **Streaming Responses**: When using `search_stream`, remember to handle the streaming nature of the response appropriately in your application.

5. **Pro Mode**: Use `pro_mode=True` when you need advanced search features, but be aware that it might be slower.

6. **Date Context**: When historical context is important for your query, always specify the `date_context` parameter.

7. **Localization**: Use the `location` and `response_language` parameters to get more relevant and localized results.

## Conclusion

The Openperplex Python library provides a powerful interface to access advanced search and web analysis capabilities. By leveraging its various methods and parameters, you can create sophisticated applications that can understand and process web content in multiple languages and contexts.

For any issues, feature requests, or further questions, please refer to the official Openperplex documentation or contact their support team.