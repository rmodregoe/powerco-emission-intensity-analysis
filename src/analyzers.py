# analyzers.py
import pandas as pd
from config import HOURS_IN_YEAR, NORTH_SEA_LAT_RANGE, NORTH_SEA_LON_RANGE

class PowerPlantAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def filter_by_country(self, country_col: str, country: str) -> pd.DataFrame:
        return self.df[self.df[country_col] == country]

    def filter_north_sea(self, lat_col: str, lon_col: str) -> pd.DataFrame:
        lat_min, lat_max = NORTH_SEA_LAT_RANGE
        lon_min, lon_max = NORTH_SEA_LON_RANGE
        return self.df[
            self.df[lat_col].between(lat_min, lat_max) &
            self.df[lon_col].between(lon_min, lon_max)
        ]

    @staticmethod
    def select_client_plant_value(client_df: pd.DataFrame,
                                  name_col: str, name: str,
                                  value_col: str) -> float:
        return (client_df[client_df[name_col] == name][value_col].values[0])

    @staticmethod
    def calculate_load_proportions(gen_df: pd.DataFrame) -> tuple:
        df = gen_df[gen_df['Type of plant']
            .isin(['Without waste heat boiler','With waste heat boiler','With downstream steam turbine'])]
        peak_proportion = df.loc[df['Type of plant']=='Without waste heat boiler',
                      'Bottleneck capacity (MW)'].sum() / df['Bottleneck capacity (MW)'].sum()
        base_proportion = 1 - peak_proportion
        return peak_proportion, base_proportion


class CapacityFactorAnalyzer:
    @staticmethod
    def calculate_capacity_factor(df: pd.DataFrame,
                gen_col="Generation (GWh)",
                cap_col="Capacity (MW)") -> pd.DataFrame:
        df["Capacity Factor"] = df[gen_col] / (df[cap_col] * HOURS_IN_YEAR)
        return df
    
    @staticmethod
    def average_capacity_factor(df, value_col):
        """Calculate the average capacity factor from a DataFrame."""
        return df[value_col].mean()

class EmissionAnalyzer:
    @staticmethod
    def calculate_emissions_per_mw(df: pd.DataFrame,
               e_col="Emissions (tCO2e)",
               cap_col="Capacity (MW)") -> pd.Series:
        """Calculate emissions per MW from a DataFrame."""
        df["Emissions per MW"] = df[e_col] / df[cap_col] 
        return df

    @staticmethod
    def calculate_average_emissions_per_mw(df: pd.DataFrame) -> float:
        """Calculate the average kg of emissions per MW."""
        return df["Emissions per MW"].mean() 

class EnergyCalculator:
    @staticmethod
    def calculate_energy_generation(capacity_mw: float, capacity_factor: float) -> float:
        return capacity_mw * HOURS_IN_YEAR * capacity_factor

class EmissionCalculator:
    @staticmethod
    def calculate_emission(plant_emissions_per_capacity: float, plant_capacity: float)-> float:
        "Calculates emissions depending on the plant capacity"
        return (plant_emissions_per_capacity * plant_capacity)
    @staticmethod
    def calculate_emission_intensity(emissions_kg: float, generation_mwh: float) -> float:
        return emissions_kg / generation_mwh