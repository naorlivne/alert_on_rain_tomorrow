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
        Will run a terraform apply on a workspace & will pass all variables to the terraform apply as terraform
        variables

        Arguments:
            :param variables: the variables to pass to the terraform apply command
            :param parallelism: the number of parallel resource operations

        Returns:
            :return return_code: the return code of the terraform apply
            :return stdout: the stdout stream of the terraform apply
            :return stderr: the stderr stream of the terraform apply
        """
        if variables is None:
            variables = {}

        return_code, stdout, stderr = self.tf.apply(no_color=IsFlagged, var=variables, skip_plan=True,
                                                    parallelism=parallelism)
        return return_code, stdout, stderr
