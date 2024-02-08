# it's offical so i'm using it + alpine so damn small
FROM python:3.12.2-alpine3.18

# set python to be unbuffered
ENV PYTHONUNBUFFERED=1

# install requirements
COPY requirements.txt /alert_on_rain_tomorrow/requirements.txt
RUN pip install -r /alert_on_rain_tomorrow/requirements.txt

# copy the codebase
COPY . /alert_on_rain_tomorrow
RUN chmod +x /alert_on_rain_tomorrow/alert_on_rain_tomorrow.py

# and running it
WORKDIR /alert_on_rain_tomorrow
CMD ["python", "/alert_on_rain_tomorrow/alert_on_rain_tomorrow.py"]
