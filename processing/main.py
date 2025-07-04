import pandas as pd
import os
from processor import normalize_data 

def main():
    input_file = "validated_employee_data.csv" 
    output_file = "processed_employee_data.csv"

    if not os.path.exists(input_file):
        print("Validated data not found. Run the ingestion phase first.")
        return

    df = pd.read_csv(input_file)
    df = normalize_data(df)
    df.to_csv(output_file, index=False)

    print("Data normalization complete. Output saved as:", output_file)

if __name__ == "__main__":
    main()
