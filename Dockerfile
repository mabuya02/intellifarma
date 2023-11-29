# Use an official Python runtime as the base image
FROM python:3.10-slim-buster as builder

# Create and set the working directory in the builder container
WORKDIR /app

# Copy just the requirements file initially to leverage Docker caching
COPY ./requirements.txt /app/

# Install dependencies within a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Start a new stage for the final image
FROM python:3.10-slim-buster

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create a non-root user and set the working directory in the final image
RUN adduser --disabled-password --gecos '' appuser && \
    mkdir -p /app && \
    chown -R appuser /app

WORKDIR /app

# Copy installed dependencies from the builder image
COPY --from=builder /venv /venv
COPY . /app/

# Expose the port your app runs on
EXPOSE 5000

# Switch to the non-root user
USER appuser

# Command to run the application using Gunicorn
CMD ["/venv/bin/gunicorn", "-b", "0.0.0.0:5000", "run:app"]
