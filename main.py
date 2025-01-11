import asyncio
from utils.scraper import crawl_domain
import json
import os

async def main(domains):
    results = {}

    # Create output directory if not exists
    os.makedirs("output", exist_ok=True)

    # Crawl each domain asynchronously
    tasks = [crawl_domain(domain) for domain in domains]
    domain_results = await asyncio.gather(*tasks)

    # Combine results
    for domain, urls in zip(domains, domain_results):
        results[domain] = urls

    # Save results to a JSON file
    with open("output/results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Crawling completed! Results saved to output/results.json")

if __name__ == "__main__":
    # Example domains for testing
    domains = [
        "https://www.amazon.com",
        "https://www.ebay.com",
        "https://www.walmart.com",
        "https://www.flipkart.com",
    ]
    asyncio.run(main(domains))

