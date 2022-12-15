# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the necessary dependencies
RUN pip install requests argparse

# When the container launches, spawn an interactive shell
CMD ["/bin/bash"]
