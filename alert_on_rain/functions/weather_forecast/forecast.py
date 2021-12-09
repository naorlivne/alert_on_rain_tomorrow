from pyowm.utils import timestamps
from pyowm.owm import OWM


class WeatherForecast:

    def __init__(self, api_key: str, city: str, country_code: str):
        """
        Will create a OWM object daily forecaster object

        Arguments:
            :param api_key: the OpenWeatherMap api key
            :param city: the city where to get the prediction for, use https://openweathermap.org/find to locate yours
            :param country_code: the 2 capital letters country code where the city is located at
            if not set
        """

        owm = OWM(api_key)
        self.mgr = owm.weather_manager()
        self.three_hour_forecast = self.mgr.forecast_at_place(city + "," + country_code, '3h')

    def rain_tomorrow(self) -> bool:
        """
        Checks if it will rain tomorrow

        Returns:
            :return bool, True if it will be rainy, False otherwise

        """
        tomorrow = timestamps.tomorrow()
        return self.three_hour_forecast.will_be_rainy_at(tomorrow)

    def storm_tomorrow(self) -> bool:
        """
        Checks if it will be stormy tomorrow

        Returns:
            :return bool, True if stormy, False otherwise

        """
        tomorrow = timestamps.tomorrow()
        return self.three_hour_forecast.will_be_stormy_at(tomorrow)
