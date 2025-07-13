import json
from C3scraper import run_scraper

def main():
    project_id = "employee_scraper"  

    with open("ingestion/run_scraper.json", "r") as f:
        configs = json.load(f)

    config = next((c for c in configs if c.get("project_id") == project_id), None)

    if not config:
        print(f"No config found for project_id: {project_id}")
        return

    print(f"Running scraper: {config['scraper_id']}")
    run_scraper(config["url"])
    print("Scraper completed successfully.")

if __name__ == "__main__":
    main()

