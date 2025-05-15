import re


class CoordinateConverter:
    @staticmethod
    def dms_to_decimal(dms_str):
        """Convert DMS (degrees, minutes, seconds) to decimal degrees."""
        if not isinstance(dms_str, str):
            return None
        match = re.match(r"(\d+)°(\d+)′(\d+)", dms_str)
        if match:
            degrees, minutes, seconds = map(int, match.groups())
            return degrees + (minutes / 60) + (seconds / 3600)
        return None

    @staticmethod
    def convert_coordinates(df, lat_col, lon_col):
        """Convert latitude and longitude columns in a DataFrame."""
        df[lat_col] = df[lat_col].apply(CoordinateConverter.dms_to_decimal)
        df[lon_col] = df[lon_col].apply(CoordinateConverter.dms_to_decimal)
        return df
