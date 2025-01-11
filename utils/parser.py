import re

def get_patterns_for_domain(domain):
    """Return URL patterns specific to a domain."""
    domain_patterns = {
        "amazon.com": [r"/dp/", r"/gp/", r"/product/"],
        "ebay.com": [r"/itm/", r"/sch/"],
        "walmart.com": [r"/ip/", r"/product/"],
        "flipkart.com": [r"/p/", r"/product/"],
        "myntra.com": [r"/buy/", r"/product/"],
        "snapdeal.com": [r"/product/"],
        "newegg.com": [r"/p/", r"/product/"]
    }
    
    for key, patterns in domain_patterns.items():
        if key in domain:
            return patterns

    # Default patterns for unknown domains
    return [r"/product/", r"/p/", r"/item/"]

def extract_product_urls(domain, soup):
    """Extract product URLs based on domain-specific patterns."""
    patterns = get_patterns_for_domain(domain)
    product_urls = set()

    # Find all <a> tags and extract href
    for link in soup.find_all("a", href=True):
        url = link["href"]
        for pattern in patterns:
            if re.search(pattern, url):
                # Handle relative URLs
                if url.startswith("/"):
                    url = domain.rstrip("/") + url
                product_urls.add(url)

    return product_urls
