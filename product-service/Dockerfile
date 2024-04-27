# Use the official Ubuntu 20.04 image as base
FROM continuumio/miniconda3

# Base Image Maintainer
MAINTAINER Lalit Kumar <2022MT93720@wilp.bits-pilani.ac.in>

# Update apt package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y python3.9 && \
    apt-get install -y python3-pip && \
    apt-get clean

# Upgrade pip to the latest version
RUN python3.9 -m pip install --upgrade pip

# Set the working directory
WORKDIR /product-service

# Copy the current directory contents into the container at /app
COPY . /product-service

# 
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python3", "app.py"]