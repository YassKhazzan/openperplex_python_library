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
from openperplex import OpenperplexSync, OpenperplexAsync

api_key = "your_openperplex_api_key_here"
client_sync = OpenperplexSync(api_key)
client_async = OpenperplexAsync(api_key)
```

## Available Methods

The library provides both synchronous and asynchronous versions of its methods. Here are the available methods:

### 1. search / search_stream

Perform a search query, either as a single response or as a stream.

#### Synchronous:

```python
# Non-streaming search
result = client_sync.search(
    query="What are the latest developments in AI?",
    date_context="2024-08-25",
    location="us",
    pro_mode=False,
    response_language="en",
    answer_type="text",
    verbose_mode=False,
    search_type="general",
    return_citations=False,
    return_sources=False,
    return_images=False
)

print(result)

# Streaming search
for chunk in client_sync.search_stream(
    query="Explain quantum computing",
    date_context="2024-08-25",
    location="us",
    pro_mode=False,
    response_language="en",
    answer_type="text",
    verbose_mode=False,
    search_type="general",
    return_citations=False,
    return_sources=False,
    return_images=False
):
    print(chunk)
```

#### Asynchronous:

```python
import asyncio

async def search_async():
    # Non-streaming search
    result = await client_async.search(
        query="What are the latest developments in AI?",
        date_context="2024-08-25",
        location="us",
        pro_mode=False,
        response_language="en",
        answer_type="text",
        verbose_mode=False,
        search_type="general",
        return_citations=False,
        return_sources=False,
        return_images=False
    )
    print(result)

    # Streaming search
    async for chunk in client_async.search_stream(
        query="Explain quantum computing",
        date_context="2024-08-25",
        location="us",
        pro_mode=False,
        response_language="en",
        answer_type="text",
        verbose_mode=False,
        search_type="general",
        return_citations=False,
        return_sources=False,
        return_images=False
    ):
        print(chunk)

asyncio.run(search_async())
```

### 2. get_website_text

Retrieve the text content of a website.

#### Synchronous:

```python
result = client_sync.get_website_text("https://www.example.com")
print(result)
```

#### Asynchronous:

```python
result = await client_async.get_website_text("https://www.example.com")
print(result)
```

### 3. get_website_screenshot

Get a screenshot of a website.

#### Synchronous:

```python
result = client_sync.get_website_screenshot("https://www.example.com")
print(result)
```

#### Asynchronous:

```python
result = await client_async.get_website_screenshot("https://www.example.com")
print(result)
```

### 4. get_website_markdown

Get the markdown representation of a website.

#### Synchronous:

```python
result = client_sync.get_website_markdown("https://www.example.com")
print(result)
```

#### Asynchronous:

```python
result = await client_async.get_website_markdown("https://www.example.com")
print(result)
```

### 5. query_from_url

Perform a query based on the content of a specific URL.

#### Synchronous:

```python
response = client_sync.query_from_url(
    url="https://www.example.com/article",
    query="What is the main topic of this article?",
    response_language="en",
    answer_type="text"
)
print(response)
```

#### Asynchronous:

```python
response = await client_async.query_from_url(
    url="https://www.example.com/article",
    query="What is the main topic of this article?",
    response_language="en",
    answer_type="text"
)
print(response)
```

### 6. custom_search / custom_search_stream

Perform a custom search query with a system prompt and user prompt.

#### Synchronous:

```python
# Non-streaming custom search
result = client_sync.custom_search(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us",
    pro_mode=False,
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9
)
print(result)

# Streaming custom search
for chunk in client_sync.custom_search_stream(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us",
    pro_mode=False,
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9
):
    print(chunk)
```

#### Asynchronous:

```python
# Non-streaming custom search
result = await client_async.custom_search(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us",
    pro_mode=False,
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9
)
print(result)

# Streaming custom search
async for chunk in client_async.custom_search_stream(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us",
    pro_mode=False,
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9
):
    print(chunk)
```

## Parameters

### Common Parameters
- `query`: The search query or question.
- `date_context`: String Optional date for context (format: "today is 8 of october and time is 4 PM" or "YYYY-MM-DD HH:MM AM/PM"). If empty, the current date of the API server is used.
- `location`: Country code for search context. Default is "us".
- `pro_mode`: Boolean to enable or disable pro mode. Default is False.
- `response_language`: Language code for the response. Default is "auto" (auto-detect).
- `answer_type`: Type of answer format. Options are "text" (default), "markdown", or "html".
- `verbose_mode`: Boolean to enable or disable verbose mode. Default is False.
- `search_type`: Type of search to perform (general or news). Default is "general".
- `return_citations`: Boolean to indicate whether to return citations. Default is False.
- `return_sources`: Boolean to indicate whether to return sources. Default is False.
- `return_images`: Boolean to indicate whether to return images. Default is False.

### Custom Search Parameters
- `system_prompt`: The system prompt for custom search.
- `user_prompt`: The user prompt for custom search.
- `temperature`: Float value to control the randomness of the output. Default is 0.2.
- `top_p`: Float value to control the diversity of the output. Default is 0.9.
- `search_type`: Type of search to perform (general or news). Default is "general".
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

## Error Handling

The library raises `OpenperplexError` exceptions for API errors. Always wrap your API calls in try-except blocks:

```python
from openperplex import OpenperplexSync, OpenperplexError

try:
    result = client_sync.search("AI advancements")
    print(result)
except OpenperplexError as e:
    print(f"An error occurred: {e}")
```

Remember to handle potential network errors and other exceptions as needed in your application.

## Best Practices

1. **API Key Security**: Never hard-code your API key in your source code. Use environment variables or secure configuration management.

2. **Error Handling**: Always implement proper error handling to manage API errors and network issues gracefully.

3. **Asynchronous Usage**: For applications that need to handle multiple requests concurrently, consider using the asynchronous version of the client.

4. **Streaming Responses**: When using `search_stream` or `custom_search_stream`, remember to handle the streaming nature of the response appropriately in your application.

5. **Pro Mode**: Use `pro_mode=True` when you need advanced search features, but be aware that it might be slower.

6. **Date Context**: When historical context is important for your query, always specify the `date_context` parameter.

7. **Localization**: Use the `location` and `response_language` parameters to get more relevant and localized results.

## Conclusion

The Openperplex Python library provides a powerful interface to access advanced search and web analysis capabilities. By leveraging its various methods and parameters, you can create sophisticated applications that can understand and process web content in multiple languages and contexts.

For any issues, feature requests, or further questions, please open an issue.