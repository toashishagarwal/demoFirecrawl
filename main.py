from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import json
import os

# Load environment variables
load_dotenv()

# Initialize Firecrawl with your API key
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

def main():
    # Extract the product information from the scraped page
    print("\n=== Extract Book Data ===")
    extract_result = app.scrape_url(
        url="http://books.toscrape.com/",
        formats=['extract'],
        extract={
            'prompt': 'Extract all book titles and prices from this page'
        }
    )
    print("Extracted data:")
    print(json.dumps(extract_result.extract, indent=2))

if __name__ == "__main__":
    main()
