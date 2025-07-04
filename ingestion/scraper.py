import requests
import pandas as pd
import os
import time

LOCAL_FILENAME = "employee_data.csv"
MAX_RETRIES = 3

def download_file(url, filename, retries=MAX_RETRIES):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filename, "wb") as f:
                f.write(response.content)
            print("File downloaded successfully.")
            return filename
        except Exception as e:
            print(f"Download failed: {e}")
            time.sleep(2 ** attempt)
    return None

def detect_file_type(filepath):
    if filepath.endswith(".csv"):
        return "text/csv"
    elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        return "excel"
    else:
        return "unknown"

def parse_file(filepath, file_type):
    try:
        if file_type == "text/csv":
            df = pd.read_csv(filepath)
        elif "excel" in file_type:
            df = pd.read_excel(filepath, engine='openpyxl')
        else:
            raise ValueError("Unsupported file type")

        column_map = {
            "User Id": "Employee ID",
            "Phone": "Phone Number",
            "Date of birth": "Hire Date"
        }
        df.rename(columns=column_map, inplace=True)
        return df
    except Exception as e:
        print(f"Failed to parse file: {e}")
        return None

def is_valid_structure(df):
    required_columns = [
        "Employee ID",
        "First Name",
        "Last Name",
        "Email",
        "Job Title",
        "Phone Number",
        "Hire Date"
    ]
    return all(col in df.columns for col in required_columns)

def run_scraper(url):
    filepath = download_file(url, LOCAL_FILENAME)
    if not filepath:
        print("Exiting due to download failure.")
        return

    file_type = detect_file_type(filepath)
    print(f"Detected file type: {file_type}")

    df = parse_file(filepath, file_type)
    if df is None:
        print("Parsing failed.")
        return

    if not is_valid_structure(df):
        print("Data structure is invalid. Required columns are missing.")
        return

    df.to_csv("validated_employee_data.csv", index=False)
    print("Employee data validated and saved.")
 
