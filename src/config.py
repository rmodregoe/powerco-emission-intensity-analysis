import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

''' File pahts'''
POWERCO_XLSX = os.path.join(PROJECT_ROOT, "data", "Data.xlsx")
POWERCO_XLSX_SHEET = 'PowerCo Power Plants'
GLOBAL_PPP_CSV = os.path.join(PROJECT_ROOT, "data", "global-power-plants.csv") 
EMBER_CSV = os.path.join(PROJECT_ROOT, "data", "Ember_power_plant_emitters_ets.csv")
ELECTRICITY_GENERATION_XLSX = os.path.join(PROJECT_ROOT, "data", "Data.xlsx")
ELECTRICITY_GENERATION_XLSX_SHEET = 'Gas Generation Germany'
CAPACITY_FACTOR_XLSX = os.path.join(PROJECT_ROOT, "data", "Data.xlsx")
CAPACITY_FACTOR_XLSX_SHEET = 'Capacity Factors'
OFFSHORE_WIND_XLSX = os.path.join(PROJECT_ROOT, "data", "Data.xlsx")
OFFSHORE_WIND_XLSX_SHEET = 'Offshore Wind Farms Germany'

''' Thresholds and ranges'''
NORTH_SEA_LAT_RANGE = (50.99, 61.017)  # Latitude range for the North Sea
NORTH_SEA_LON_RANGE = (-4.4454, 12.0059)  # Longitude range for the North Sea
DISTANCE_THRESHOLD_DEG = 0.02 # ~ 2 km

''' Conversion Factors'''
HOURS_IN_YEAR = 8760
GWH_TO_MWH = 1000
TONS_TO_KG = 1000

''' Emsission and Capacity Factors'''
PEAK_CAPACITY_FACTOR = 0.13 #Source:https://en.wikipedia.org/wiki/Wendefurth_Power_Station)
WIND_PARK_EMISSION_INTENSITY = 20    # kg CO2e/MWh only during upstram and downstream operations, no emissions during operation. Source: https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/257062
SOLAR_PARK_EMISSION_INTENSITY = 40   # kg CO2e/MWh only during upstram and downstream operations, no emissions during operation

''' Main German Electricity Generation Companies Physical Emission Intensity'''
RWE_PHYSICAL_EMISSION_INTENSITY = 480 # kg CO2e/MWh Source: https://www.rwe.com/-/media/RWE/documents/09-verantwortung-nachhaltigkeit/cr-berichte/sustainability-strategy-report-2023.pdf
ENBW_PHYSICAL_EMISSION_INTENSITY = 343 # kg CO2e/MWh Source: https://www.enbw.com/sustainability/environment/environment-protection/co2-footprint.html
EON_PHYSICAL_EMISSION_INTENSITY = 100 # kg CO2e/MWh Source: https://www.eon.com/en/about-us/sustainability/reporting.html
VATTENFALL_EMISSIONS = 23e9  # kg CO2e Source: https://group.vattenfall.com/globalassets/com/sustainability/vattenfall-annual-and-sustainability-report-2023.pdf
VATTENFALL_GENERATION = 100.9e6  # MWh Source: https://www.statista.com/statistics/812773/vattenfall-electricity-generation-europe/