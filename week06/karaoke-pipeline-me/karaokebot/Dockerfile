#
# Dockerfile for the Karaoke Bot
#
# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install psycopg2-binary

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run 'python gloria.py' when the container launches
CMD ["python", "gloria.py"]
