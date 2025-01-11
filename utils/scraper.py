import aiohttp
from bs4 import BeautifulSoup
from utils.parser import extract_product_urls
from urllib.parse import urljoin, urlparse
import asyncio
import time

RATE_LIMIT = 5  # Max number of concurrent requests per domain
TIME_LIMIT = 120  # Time limit in seconds (2 minutes)

async def fetch_url(session, url, semaphore):
    """Fetch a URL asynchronously with rate limiting."""
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                print(f"Failed to fetch {url} with status {response.status}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return None

async def crawl_domain(domain, max_depth=3):
    """
    Crawl a domain to discover product URLs.
    Includes rate limiting and respects a time limit.
    """
    print(f"Crawling {domain}...")
    visited_urls = set()
    product_urls = set()
    semaphore = asyncio.Semaphore(RATE_LIMIT)  # Limit concurrent requests
    start_time = time.time()

    async def crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return

        # Check if the time limit has been reached
        if time.time() - start_time > TIME_LIMIT:
            print(f"Time limit reached for {domain}. Stopping...")
            return

        print(f"Visiting: {url}")
        visited_urls.add(url)

        async with aiohttp.ClientSession() as session:
            html = await fetch_url(session, url, semaphore)
            if not html:
                return

            soup = BeautifulSoup(html, "html.parser")
            product_urls.update(extract_product_urls(domain, soup))

            # Find all links on the page
            for link in soup.find_all("a", href=True):
                href = link["href"]
                # Resolve relative URLs
                full_url = urljoin(url, href)

                # Ensure the URL is within the same domain
                if urlparse(full_url).netloc == urlparse(domain).netloc:
                    await crawl(full_url, depth + 1)

    # Start crawling from the root domain
    await crawl(domain, 0)

    return list(product_urls)
