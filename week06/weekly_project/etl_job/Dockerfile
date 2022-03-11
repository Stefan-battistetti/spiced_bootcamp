#
# Dockerfile for the Karaoke Bot
#
# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app2

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
COPY requirements.txt /app2

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run 'python gloria.py' when the container launches
CMD ["python", "etl_job.py"]
