# URL Shortener API

This is a simple URL Shortener API built with Python. It allows users to shorten long URLs and retrieve the original URLs using the shortened version.

## Features

- Shorten long URLs
- Retrieve original URLs from shortened URLs
- Simple and easy-to-use API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/NeGat1FF/URL-Shortener.git
    ```
2. Navigate to the project directory:
    ```bash
    cd url-shortener
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the server:
    ```bash
    fastapi run main.py
    ```
2. Use the API endpoints to shorten URLs and retrieve original URLs.

### API Endpoints

- **POST /**
    - Request body:
        ```json
        {
            "url": "https://example.com"
        }
        ```
    - Response:
        ```json
        {
        "id": 1,
        "url": "https://example.com/",
        "short_code": "string",
        "visit_count": 0,
        "created_at": "2024-12-22T09:39:39.643Z",
        "updated_at": "2024-12-22T09:39:39.643Z"
        }
        ```

- **DELETE /<short_url>**
    - Response:
        ```json
        {
            "message": "URL deleted successfully"
        }
        ```

- **PATCH /<short_url>**
    - Request body:
        ```json
        {
            "url": "https://newexample.com"
        }
        ```
    - Response:
        ```json
        {
            "id": 1,
            "url": "https://newexample.com/",
            "short_code": "string",
            "visit_count": 0,
            "created_at": "2024-12-22T09:39:39.643Z",
            "updated_at": "2024-12-22T09:39:39.643Z"
        }
        ```

- **GET /<short_url>/info**
    - Response:
        ```json
        {
            "id": 1,
            "url": "https://example.com/",
            "short_code": "string",
            "visit_count": 10,
            "created_at": "2024-12-22T09:39:39.643Z",
            "updated_at": "2024-12-22T09:39:39.643Z"
        }
        ```

- **GET /<short_url>**
    - Response:
        ```json
        {
            "original_url": "https://example.com"
        }
        ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

https://roadmap.sh/projects/url-shortening-service
