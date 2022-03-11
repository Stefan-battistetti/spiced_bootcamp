FROM python:3.8-slim  
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /app   

RUN pip3 install matplotlib
RUN pip3 install pandas  
RUN pip install slack_sdk 
RUN pip install pytz     
RUN pip install imgurpython


COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "etl.py"]


