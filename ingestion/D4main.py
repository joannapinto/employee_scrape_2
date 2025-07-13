import json
import os
from D4scraper import (
    load_reference_data,
    load_raw_data,
    filter_and_map_data,
    save_mapped_data,
    run_scraper
)

def main():
    project_id = "data_mapper"
    config_path = os.path.join("ingestion", "run_scraper.json")

    with open(config_path, "r") as f:
        configs = json.load(f)

    config = next((c for c in configs if c.get("project_id") == project_id), None)

    if not config:
        print(f"No config found for project_id: {project_id}")
        return

    print(f"Running scraper: {config['scraper_id']}")
    run_scraper(config["url"])  # Optional step for downloading

    reference_path = os.path.join("ingestion", "D4reference_data.xlsx")
    raw_path = os.path.join("ingestion", "D4raw_data.csv")
    output_path = os.path.join("ingestion", "D4mapped_output.csv")

    reference_df = load_reference_data(reference_path)
    raw_df = load_raw_data(raw_path)
    mapped_df = filter_and_map_data(reference_df, raw_df)
    save_mapped_data(mapped_df, output_path)

    print("Scraper completed and data mapping saved to mapped_output.csv.")

if __name__ == "__main__":
    main()
