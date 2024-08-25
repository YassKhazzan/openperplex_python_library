import httpx
import json
from typing import Optional, Dict, Any, Generator, List
from urllib.parse import urljoin

class OpenperplexError(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"OPENPERPLEX ERROR : {status_code} - {detail}")

class Openperplex:
    def __init__(self, api_key: str, base_url: str = "https://5e70fd93-e9b8-4b9c-b7d9-eea4580f330c.app.bhs.ai.cloud.ovh.net"):
        self.base_url = base_url
        self.api_key = api_key
        self.client = httpx.Client(timeout=40.0)

        if not api_key:
            raise ValueError("API key is required")

    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> httpx.Response:
        url = urljoin(self.base_url, endpoint)
        headers = {
            "X-API-Key": self.api_key,
        }

        response = self.client.get(url, params=params, headers=headers)

        if response.status_code == 401:
            raise OpenperplexError(401, "Invalid Openperplex API Key")

        if not response.is_success:
            self._handle_error_response(response)
        return response

    def search_stream(self, query: str, date_context: Optional[str] = None, location: str = 'us',
                      pro_mode: bool = False, response_language: str = 'auto', answer_type: str = 'text') -> Generator[Dict[str, Any], None, None]:
        endpoint = "/search_stream"
        params = {
            "query": query,
            "date_context": date_context,
            "location": location,
            "pro_mode": pro_mode,
            "response_language": response_language,
            "answer_type": answer_type
        }

        with self.client.stream("GET", urljoin(self.base_url, endpoint), params=params, headers={
            "X-API-Key": self.api_key,
        }) as response:
            if not response.is_success:
                self._handle_error_response(response)
            yield from self._stream_sse_response(response)

    def search_simple_stream(self, query: str, location: str = 'us', date_context: Optional[str] = None,
                             pro_mode: bool = False, response_language: str = 'auto', answer_type: str = 'text') -> Generator[Dict[str, Any], None, None]:
        endpoint = "/search_simple_stream"
        params = {
            "query": query,
            "location": location,
            'date_context': date_context,
            'pro_mode': pro_mode,
            'response_language': response_language,
            'answer_type': answer_type
        }

        with self.client.stream("GET", urljoin(self.base_url, endpoint), params=params, headers={
            "X-API-Key": self.api_key,
        }) as response:
            if not response.is_success:
                self._handle_error_response(response)
            yield from self._stream_sse_response(response)

    def search(self, query: str, date_context: Optional[str] = None, location: str = 'us', pro_mode: bool = False,
               response_language: str = 'auto', answer_type: str = 'text') -> Dict[str, Any]:
        endpoint = "/search"
        params = {
            "query": query,
            "date_context": date_context,
            "location": location,
            "pro_mode": pro_mode,
            "response_language": response_language,
            "answer_type": answer_type
        }

        response = self._make_request(endpoint, params)
        return response.json()

    def search_simple(self, query: str, location: str = 'us', date_context: Optional[str] = None,
                      pro_mode: bool = False, response_language: str = 'auto', answer_type: str = 'text') -> Dict[str, Any]:
        endpoint = "/search_simple"
        params = {
            "query": query,
            "location": location,
            'date_context': date_context,
            'pro_mode': pro_mode,
            'response_language': response_language,
            'answer_type': answer_type
        }

        response = self._make_request(endpoint, params)
        return response.json()

    def get_website_text(self, url: str) -> Dict[str, Any]:
        endpoint = "/get_website_text"
        params = {"url": url}

        response = self._make_request(endpoint, params)
        return response.json()

    def get_website_screenshot(self, url: str) -> Dict[str, Any]:
        endpoint = "/get_website_screenshot"
        params = {"url": url}

        response = self._make_request(endpoint, params)
        return response.json()

    def get_website_markdown(self, url: str) -> Dict[str, Any]:
        endpoint = "/get_website_markdown"
        params = {"url": url}

        response = self._make_request(endpoint, params)
        return response.json()

    def query_from_url(self, url: str, query: str, response_language: str = 'auto', answer_type: str = 'text') -> Dict[str, Any]:
        endpoint = "/query_from_url"
        params = {"url": url, "query": query, "response_language": response_language, "answer_type": answer_type}

        response = self._make_request(endpoint, params)
        return response.json()

    def _stream_sse_response(self, response: httpx.Response) -> Generator[Dict[str, Any], None, None]:
        for line in response.iter_lines():
            if line:
                try:
                    if line.startswith("data:"):
                        data_str = line.split("data:", 1)[1].strip()
                        data = json.loads(data_str)

                        if isinstance(data, dict) and "type" in data:
                            if data["type"] == "error":
                                raise OpenperplexError(data.get("status_code", 500),
                                                       data.get("detail", "Unknown error"))
                            else:
                                yield data

                except json.JSONDecodeError:
                    print(f"Failed to parse JSON from line: {line}")
                except OpenperplexError as e:
                    raise e
                except Exception as e:
                    print(f"Error processing line: {e}")

    def _handle_error_response(self, response: httpx.Response):
        try:
            if response.status_code == 401:
                raise OpenperplexError(401, "Invalid Openperplex API Key")
            error_data = response.json() if response.content else {}
            status_code = error_data.get('status_code', response.status_code)
            detail = error_data.get('detail', 'An unknown error occurred')

            if 'OPENAI Error:' in detail:
                raise OpenperplexError(status_code, detail.split('OPENPERPLEX Error:', 1)[1].strip())
            else:
                raise OpenperplexError(status_code, f"Unexpected error: {detail}")
        except json.JSONDecodeError:
            raise OpenperplexError(response.status_code, f"Unexpected error: {response.text}")

    def __del__(self):
        self.client.close()