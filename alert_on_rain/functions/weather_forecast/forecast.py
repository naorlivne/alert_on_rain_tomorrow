from pyowm.utils import timestamps
from pyowm.owm import OWM
from typing import Tuple, Optional


class WeatherForecast:

    def __init__(self, api_key: str, city: str, country_code: str):
        """
        Will create a terraform object, create a workspace & init the terraform directory

        Arguments:
            :param api_key: the workspace terraform will be executed in
            :param city: the full path of the folder to run the terraform in
            :param country_code: the full path of the terraform binary to use, will try to use the one at the path
            if not set
        """

        # TODO below is a copy paste example that needs splitting up and work
        from pyowm.utils import timestamps
        from pyowm.owm import OWM
        owm = OWM('your-api-key')
        mgr = owm.weather_manager()
        three_h_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')

        # Is it going to rain tomorrow?
        tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
        three_h_forecaster.will_be_rainy_at(tomorrow)

    def rain_tomorrow(self, variables: Optional[dict] = None, parallelism: int = 10) -> Tuple[str, str, str]:
        """

        """
        pass