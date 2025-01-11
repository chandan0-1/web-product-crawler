README: E-Commerce Product URL Crawler

## Overview
This project implements a web crawler for discovering product URLs on e-commerce websites. It intelligently handles nested URLs, supports rate limiting, and respects a time limit for crawling each domain.

## Features
* **Domain-Specific Patterns** : Detects product URLs using domain-specific heuristics.
* **Nested URL Crawling** : Recursively crawls pages to discover deeply nested product URLs.
* **Rate Limiting** : Controls the number of concurrent requests to prevent overloading servers.
* **Time Limit** : Ensures the crawler stops after 2 minutes for each domain.
* **Output** : Saves discovered product URLs in a structured JSON file.

## Setup

1. Prerequisites
Python 3.7 or above.
Install required Python packages:

```bash 
pip install -r requirements.txt
```

2. Clone the Repository

```bash
git clone git@github.com:chandan0-1/web-product-crawler.git
cd web-product-crawler
```

3. Directory Structure
```graphql
web-product-crawler/
├── main.py              # Entry point of the application
├── utils/
│   ├── scraper.py       # Crawling logic with rate limiting and time limit
│   ├── parser.py        # Extracts product URLs using domain-specific patterns
├── output/
│   └── results.json     # Output file with discovered product URLs
├── requirements.txt     # Dependency file for Python packages
└── README.md            # Documentation
```

## Usage
1. Add Domains
Edit the main.py file and add the domains you want to crawl:
```python3
if __name__ == "__main__":
    domains = [
        "https://www.amazon.com",
        "https://www.ebay.com",
        "https://example.com"
    ]
    asyncio.run(main(domains))
```

2. Run the Crawler
Execute the script:
```bash
python main.py
```

* Alternative For Python3
```bash
python3 main.py
```

3. Output
The crawler saves results in output/results.json:
```json
{
  "https://www.amazon.com": [
    "https://www.amazon.com/dp/B08N5WRWNW",
    "https://www.amazon.com/gp/product/B07XQXZXJC"
  ],
  "https://www.ebay.com": [
    "https://www.ebay.com/itm/123456789"
  ]
}
```

## Configuration
1. Rate Limiting
Set the maximum number of concurrent requests in utils/scraper.py:

```python3
RATE_LIMIT = 5  # Default is 5
```

2. Time Limit
Adjust the time limit for each domain crawl:

```python3
TIME_LIMIT = 120  # Default is 120 seconds (2 minutes)
```

3. Depth of Crawling
Control the maximum depth of recursive crawling:

```python3
max_depth=3  # Adjust in the crawl_domain function
```


## Testing
1. Test Domains:
* Add real-world domains with nested product URLs.
* Example: `https://www.amazon.com`, `https://www.ebay.com`.

2. Logs:
* Monitor the console output for crawling progress and errors.

3. Partial Results:
* Check `output/results.json` for URLs discovered within the time limit.

## Future Enhancements
* Support for JavaScript-rendered content using tools like Playwright or Selenium.
* Graceful shutdown with intermediate result saving.
* Dynamic rate limiting based on server response times.
