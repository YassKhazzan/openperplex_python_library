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

- **Query Precision**: Provide clear and concise queries to get accurate results.



#### Synchronous:

```python
# Non-streaming search
result = client_sync.search(
    query="What are the latest developments in AI?",
    date_context="Today is Tuesday 19 of November 2024 and the time is 9:40 PM",
    location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    response_language="en", # can be 'auto', 'en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'ja', 'ko', 'zh', 'ar', 'ru', 'tr', 'hi'
    answer_type="text", # can be 'text', 'markdown', or 'html'
    search_type="general", # can be 'news' or 'general'
    return_citations=False, # set to True to return citations
    return_sources=False, # set to True to return sources
    return_images=False, #set to True to return images (depends on the query, some queries may not return images)
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
)

print(result)

# Streaming search
for chunk in client_sync.search_stream(
    query="Explain quantum computing",
    date_context="Today is Tuesday 19 of November 2024 and the time is 9:40 PM",
    location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
    response_language="en", # can be 'auto', 'en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'ja', 'ko', 'zh', 'ar', 'ru', 'tr', 'hi'
    answer_type="text", # can be 'text', 'markdown', or 'html'
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    search_type="general", # can be 'news' or 'general'
    return_citations=False, # set to True to return citations
    return_sources=False, # set to True to return sources
    return_images=False, #set to True to return images (depends on the query, some queries may not return images)
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
):
    print(chunk)
```

#### Asynchronous:

```python
import asyncio

# Non-streaming search
async def search_async():    
    result = await client_async.search(
        query="What are the latest developments in AI?",
        date_context="Today is Tuesday 19 of November 2024 and the time is 9:40 PM",
        location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
        response_language="en", # can be 'auto', 'en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'ja', 'ko', 'zh', 'ar', 'ru', 'tr', 'hi'
        answer_type="text", # can be 'text', 'markdown', or 'html'
        model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
        search_type="general", # can be 'news' or 'general'
        return_citations=False, # set to True to return citations
        return_sources=False, # set to True to return sources
        return_images=False, #set to True to return images (depends on the query, some queries may not return images)
        recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
    )
    print(result)

# Streaming search
async for chunk in client_async.search_stream(
        query="Explain quantum computing",
        date_context="Today is Tuesday 19 of November 2024 and the time is 9:40 PM",
        location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
        response_language="en", # can be 'auto', 'en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'ja', 'ko', 'zh', 'ar', 'ru', 'tr', 'hi'
        answer_type="text", # can be 'text', 'markdown', or 'html'
        model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
        search_type="general", # can be 'news' or 'general'
        return_citations=False, # set to True to return citations
        return_sources=False, # set to True to return sources
        return_images=False, #set to True to return images
        recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
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
    response_language="en", # can be 'auto', 'en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'ja', 'ko', 'zh', 'ar', 'ru', 'tr', 'hi'
    answer_type="text", # can be 'text', 'markdown', or 'html'
     model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
)
print(response)
```

#### Asynchronous:

```python
response = await client_async.query_from_url(
    url="https://www.example.com/article",
    query="What is the main topic of this article?",
    response_language="en", 
    answer_type="text",
    model="o3-mini-medium" # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
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
    location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    search_type="general", # can be 'news' or 'general'
    return_images=False, # set to True to return images
    return_sources=False, # set to True to return sources
    temperature=0.2, # float value to control the randomness of the output
    top_p=0.9, # float value to control the diversity of the output
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
)
print(result)

# Streaming custom search
for chunk in client_sync.custom_search_stream(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9,
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
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
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    search_type="general",
    return_images=False,
    return_sources=False,
    temperature=0.2,
    top_p=0.9,
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
)
print(result)

# Streaming custom search
async for chunk in client_async.custom_search_stream(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain the theory of relativity",
    location="us", # can be 'us', 'ca', 'uk',.... (see supported locations below)
    model="o3-mini-medium", # can be 'o3-mini-medium', 'o3-mini-high', 'gpt-4o', 'gpt-4o-mini'
    search_type="general", # can be 'news' or 'general'
    return_images=False, # set to True to return images
    return_sources=False, # set to True to return sources
    temperature=0.2, # float value to control the randomness of the output
    top_p=0.9, # float value to control the diversity of the output
    recency_filter="anytime" # can be 'hour', 'day', 'week', 'month', 'year', 'anytime'
):
    print(chunk)
```

## Parameters

### Common Parameters for Search Methods
- `query`: The search query or question.
- `date_context`: String Optional date for context (format: "today is 8 of october and time is 4 PM" or "YYYY-MM-DD HH:MM AM/PM"). If empty, the current date of the API server is used.
- `location`: Country code for search context. Default is "us".
- `model`: Model to use for the search. Options are "o3-mini-medium", "o3-mini-high", "gpt-4o", or "gpt-4o-mini"(default).
- `response_language`: Language code for the response. Default is "auto" (auto-detect).
- `answer_type`: Type of answer format. Options are "text" (default), "markdown", or "html".
- `search_type`: Type of search to perform (general or news). Default is "general".
- `return_citations`: Boolean to indicate whether to return citations. Default is False.
- `return_sources`: Boolean to indicate whether to return sources. Default is False.
- `return_images`: Boolean to indicate whether to return images. Default is False.
- `recency_filter`: Filter results by recency. Options are "hour", "day", "week", "month", "year", or "anytime". Default is "anytime".

### Custom Search Parameters
- `system_prompt`: The system prompt for custom search.
- `user_prompt`: The user prompt for custom search.
- `model`: Model to use for the search. Options are "o3-mini-medium", "o3-mini-high", "gpt-4o", or "gpt-4o-mini"(default).
- `temperature`: Float value to control the randomness of the output. Default is 0.2.
- `top_p`: Float value to control the diversity of the output. Default is 0.9.
- `search_type`: Type of search to perform (general or news). Default is "general".
- `return_images`: Boolean to indicate whether to return images. Default is False.
- `return_sources`: Boolean to indicate whether to return sources. Default is False.
- `recency_filter`: Filter results by recency. Options are "hour", "day", "week", "month", "year", or "anytime". Default is "anytime".
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

## Best Practices
- **Query Precision**: Provide clear and concise queries to get accurate results.
- **Custom Search**: Use the `custom_search` or `custom_search_stream` to write your own system and user prompts for more specific queries. always be specific with the user prompt since it will be used for the web search. Remember to include date context if needed in your system prompt. if you need citations, you must add the citation prompt in the System prompt.
- **API Key Security**: Never hard-code your API key in your source code. Use environment variables or secure configuration management.
- **Error Handling**: Always implement proper error handling to manage API errors and network issues gracefully.
- **Asynchronous Usage**: For applications that need to handle multiple requests concurrently, consider using the asynchronous version of the client.
- **Streaming Responses**: When using `search_stream` or `custom_search_stream`, remember to handle the streaming nature of the response appropriately in your application.
- **model**: Use the `model` parameter to specify the model to use for the search. The default model is "gpt-4o-mini". Other options are "o3-mini-high","o3-mini-medium", "gpt-4o", or "gpt-4o-mini".
- **Date Context**: When historical context is important for your query, always specify the `date_context` parameter. Use the format "Today is Tuesday 19 of November 2024 and the time is 9:40 PM".
- **Localization**: Use the `location` to get localized results.
- **Response Language**: Use the `response_language` parameter to get responses in different languages.
- **Recency Filter**: Use the `recency_filter` parameter to filter results by recency.
- **Search Type**: Use the `search_type` parameter to specify the type of search (general or news).


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

## Discord Community
- Join our Discord community to get help, share your projects, and discuss the latest updates: [Openperplex Discord](https://discord.com/invite/rdZQPEQGMc)

## Conclusion

The Openperplex Python library provides a powerful interface to access advanced search and web analysis capabilities. By leveraging its various methods and parameters, you can create sophisticated applications that can understand and process web content in multiple languages and contexts.

For any issues, feature requests, or further questions, please open an issue.

