from weather_data import WeatherData
#Hello World

if __name__ == '__main__':
    data = WeatherData('AU540')

    print(data.barometric_pressure_pa)
