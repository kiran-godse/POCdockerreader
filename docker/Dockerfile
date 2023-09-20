# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Compile the Python file (replace 'your-python-file.py' with the actual filename)
RUN python -m py_compile your-python-file.py

# Specify the command to run your application
CMD [ "python", "src/app.py" ]
