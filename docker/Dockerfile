# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the src/app.py file into the Docker build context
COPY src/app.py /app

# Compile the Python file
RUN python -m py_compile app.py

# Specify the command to run your application
CMD [ "python", "app.py" ]
