import unittest
import pandas as pd
from unittest.mock import patch
from ingestion.D4scraper import filter_and_map_data, save_mapped_data

class TestScraper4(unittest.TestCase):

    def setUp(self):
        # Simulated reference data (Excel)
        self.reference_data = pd.DataFrame({
            "ID": [1, 2, 3, 4],
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Department": ["HR", "Finance", "IT", "Marketing"]
        })

        # Simulated raw data with duplicate ID
        self.raw_data = pd.DataFrame({
            "ID": [2, 4, 2]  # Duplicate
        })

