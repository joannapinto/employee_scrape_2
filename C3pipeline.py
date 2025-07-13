import os

print("Starting full pipeline...")

# Run ingestion
print("\nRunning ingestion:")
os.system("python ingestion/C3main.py")

# Run processing
print("\nRunning processing:")
os.system("python processing/C3main3.py")

print("\nPipeline completed successfully.")
