    # alert_on_rain_tomorrow

A simple job designed to run inside a cron wrapper of some sort (pick your poison as each orchestrator/cloud provider has its own way of doing scheduled jobs nowadays) that will alert via telegram & email when it looks like it will rain tomorrow then exit (it's not long-running as again it's designed to run inside a cron scheduler of some kind).

Drone.io CI/CD unit tests & auto push status: [![Build Status](https://cloud.drone.io/api/badges/naorlivne/alert_on_rain_tomorrow/status.svg)](https://cloud.drone.io/naorlivne/alert_on_rain_tommrrow)

Code coverage: [![codecov](https://codecov.io/gh/naorlivne/alert_on_rain_tomorrow/branch/master/graph/badge.svg)](https://codecov.io/gh/naorlivne/alert_on_rain_tomorrow)

# Running

The container will run with the following command, check for rain tomorrow and alert if it looks like a rainy day then exit, It's designed to run under some cron scheduler (k8s, metronome/mesos or linux OS cron), below is the example command needed to run the container one off

```shell
docker run -e OWM_API_KEY="my_owm_token" -e CITY="Tel Aviv" -e COUNTRY_CODE="IL" -e SMTP_SERVER="smtp.gmail.com" -e SENDER_EMAIL="mymail@example.com" -e RECEIVER_EMAIL="mymail@example.com" -e EMAIL_PASSWORD="pass" -e EMAIL_PORT="465" -e TELEGRAM_TOKEN="my_token" -e CHAT_ID="123" naorlivne/alert_on_rain_tomorrow
```

# Configuration options

alert_on_rain_tomorrow uses sane defaults, but they can all be easily changed:

| value                  | envvar                 | default value          | notes                                                                                                  |
|------------------------|------------------------|------------------------|--------------------------------------------------------------------------------------------------------|
|  owm_api_key           | OWM_API_KEY            |                        | You can get a free one at https://openweathermap.org/                                                  |
|  city                  | CITY                   |                        | The city you want to be alerted should it rain tomorrow                                                |
|  country_code          | COUNTRY_CODE           |                        | The 2 capital letters country code where the city is located at                                        |
| smtp_server            | SMTP_SERVER            |                        | SMTP server address which mail is sent through (SSL/TLS enabled)                                       |
| sender_email           | SENDER_EMAIL           |                        | Email address to send the alert out of                                                                 |
| receiver_email         | RECEIVER_EMAIL         |                        | Email address to send the alert to                                                                     |
| email_password         | EMAIL_PASSWORD         |                        | `sender_email` account password                                                                        |
| email_port             | EMAIL_PORT             |                        | SMTP server port                                                                                       |
| telegram_token         | TELEGRAM_TOKEN         |                        | Telegram API token                                                                                     |
| chat_id                | CHAT_ID                |                        | Telegram `chat_id` with the bot which you'll be alerted through                                        |

The easiest way to change a default value is to pass the envvar key\value to the docker container with the `-e` cli arg but if you want you can also create a configuration file with the settings you wish (in whatever of the standard format you desire) & place it in the /www/config folder inside the container.

Most providers also allow setting their configuration access_keys\etc via envvars use `-e` cli args to configure them is ideal as well but should you wish to configure a file you can also easily mount\copy it into the container as well.
