import os

print("Starting full pipeline...")

# Run ingestion
print("\nRunning ingestion:")
os.system("python ingestion/D4main.py")

# Run processing
print("\nRunning processing:")
os.system("python processing/D4main.py")

print("\nPipeline completed successfully.")
