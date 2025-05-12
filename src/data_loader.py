import pandas as pd
from config import GLOBAL_PPP_CSV, EMBER_CSV

class DataLoader:
    """Handles loading data from Excel or CSV files."""
    @staticmethod
    def load_excel(file_path, sheet_name):
        """Load data from an Excel sheet."""
        try:
            return pd.read_excel(file_path, sheet_name=sheet_name)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        except Exception as e:
            print(f"Error loading data: {e}")
        return None

    @staticmethod
    def load_csv(file_path):
        """Load data from a CSV file."""
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        except Exception as e:
            print(f"Error loading data: {e}")
        return None
    
    @staticmethod
    def load_global_power_plants() -> pd.DataFrame:
        df = pd.read_csv(GLOBAL_PPP_CSV, usecols=[
            "name","latitude","longitude",
            "estimated_generation_gwh_2017","capacity_mw"
        ])
        return df.rename(columns={
            "name": "Name",
            "latitude": "Lat",
            "longitude":"Long",
            "estimated_generation_gwh_2017":"Generation (GWh)",
            "capacity_mw":"Capacity (MW)"
        })

    @staticmethod
    def load_ember_power_plants() -> pd.DataFrame:
        df = pd.read_csv(EMBER_CSV, usecols=["Name","Lat","Long","2022"])
        return df.rename(columns={"2022":"Emissions (tCO2e)"})