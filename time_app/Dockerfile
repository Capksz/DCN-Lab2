#Emos Ker ck3189
FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

RUN pip install Flask pytz

COPY . .

CMD [ "python", "./run.py" ]
