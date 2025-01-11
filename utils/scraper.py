import aiohttp
from bs4 import BeautifulSoup
from utils.parser import extract_product_urls

async def fetch_url(session, url):
    """Fetch a URL asynchronously."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            print(f"Failed to fetch {url} with status {response.status}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

async def crawl_domain(domain):
    """Crawl a single domain to find product URLs."""
    print(f"Crawling {domain}...")
    product_urls = set()

    async with aiohttp.ClientSession() as session:
        html = await fetch_url(session, domain)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            product_urls.update(extract_product_urls(domain, soup))

    return list(product_urls)
