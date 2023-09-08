# Use an official Python runtime as a parent image
FROM python:3.9-alpine

#upgrading pip
RUN pip install --upgrade pip 

# Set working directory
WORKDIR /ecom

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .
