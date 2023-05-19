import requests


class WeatherData(object):
    """
    Weather Data is an object that contains weather data from a specific observation station.
    """

    def __init__(self, station_id):
        station_data = requests.get(f'https://api.weather.gov/stations/{station_id}/observations/latest').json()
        properties = station_data['properties']
        # stationProperties = ['dewpoint', 'windDirection', 'windSpeed', 'windGusts' ]

        self.dewpoint_c = properties['dewpoint']['value']  # Degrees Celsius
        """Dewpoint in degrees celsius."""

        self.wind_direction_deg = properties['windDirection']['value']  # degrees
        """Wind direction in degrees."""

        self.wind_speed_kmph = properties['windSpeed']  # Kilometers per Hour
        """Wind speed in kilometers per hour."""

        self.wind_gust_kmh = properties['windGust']['value']  # Kilometers per Hour
        """Maximum wind gust speed in kilometers per hour."""

        self.barometric_pressure_pa = properties['barometricPressure']['value']  # pascals
        """Barometric pressure in pascals."""

        self.visibility_m = properties['visibility']['value']  # Meters
        """Visibility distance in meters."""

        self.max_temp_c = properties['maxTemperatureLast24Hours']  # Degrees Celsius
        """Maximum temperature in the last 24 hours in degrees celsius."""

        self.min_temp_c = properties['minTemperatureLast24Hours']  # Degrees Celsius
        """Minimum temperature in the last 24 hours in degrees celsius."""

        self.relative_humidity = properties['relativeHumidity']['value']  # %
        """Relative humidity in percent."""

        self.wind_chill_c = properties['windChill']['value']  # Degrees Celsius
        """Wind chill in degrees celsius"""

        self.heat_index_c = properties['heatIndex']['value']  # Degrees Celsius
        """Heat index in degrees celsius."""
