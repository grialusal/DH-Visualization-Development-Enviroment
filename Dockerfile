# Use an official Python runtime as a parent image
FROM python:3-onbuild

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./requirements.txt /tmp/req.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME templateFlaskPythonD3

# run the application
CMD ["python", "./app/app.py"]
RUN mkdir /data

