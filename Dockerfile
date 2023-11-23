# Use an official Python runtime as the base image
FROM python:3.10-slim-buster


# Create and set the working directory in the container
WORKDIR /app

# Copy just the requirements file initially to leverage Docker caching
COPY ./requirements.txt /app/

# Install dependencies within a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app/

# Expose the port your app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application using Gunicorn
CMD ["/venv/bin/gunicorn", "-b", "0.0.0.0:5000", "run:app"]

