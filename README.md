    # alert_on_rain_tomorrow

A simple job designed to run inside a cron wrapper of some sort (pick your poison as each orchestrator/cloud provider has it's own way of doing scheduled jobs nowadays) that will alert via telegram & email when it looks like it will rain tomorrow then exit (it's not long running as again it's designed to run inside a cron scheduler of some kind).

Drone.io CI/CD unit tests & auto push status: [![Build Status](https://cloud.drone.io/api/badges/naorlivne/alert_on_rain_tomorrow/status.svg)](https://cloud.drone.io/naorlivne/alert_on_rain_tommrrow)

Code coverage: [![codecov](https://codecov.io/gh/naorlivne/alert_on_rain_tomorrow/branch/master/graph/badge.svg)](https://codecov.io/gh/naorlivne/alert_on_rain_tomorrow)

# Running



# Configuration options

alert_on_rain_tomorrow uses sane defaults but they can all be easily changed:

| value                  | envvar                 | default value          | notes                                                                                                  |
|------------------------|------------------------|------------------------|--------------------------------------------------------------------------------------------------------|
|  owm_api_key           | OWM_API_KEY            |                        | You can get a free one at https://openweathermap.org/                                                  |
|  city                  | CITY                   |                        | The city you want to be alerted should it rain tomorrow                                                |
|  country_code          | COUNTRY_CODE           |                        | The 2 capital letters country code where the city is located at                                        |

The easiest way to change a default value is to pass the envvar key\value to the docker container with the `-e` cli arg but if you want you can also create a configuration file with the settings you wish (in whatever of the standard format you desire) & place it in the /www/config folder inside the container.

Most providers also allow setting their configuration access_keys\etc via envvars use `-e` cli args to configure them is ideal as well but should you wish to configure a file you can also easily mount\copy it into the container as well.
