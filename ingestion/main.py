import json
import os
from scraper import run_scraper

def main():
    config_path = os.path.join("ingestion", "run_scraper.json")

    if not os.path.exists(config_path):
        print("Config file not found:", config_path)
        return

    with open(config_path, 'r') as f:
        config = json.load(f)

    print(f"Running scraper: {config.get('scraper_id', 'Unnamed')}")
    run_scraper(config['url'])
    print("Scraper completed all tasks successfully.")

if __name__ == "__main__":
    main()
