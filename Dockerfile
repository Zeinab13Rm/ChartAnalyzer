# Stage 1: Base image with Python
FROM python:3.12-slim AS base
# Set working directory inside the container
WORKDIR /app
# Prevent Python from writing .pyc files and ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Stage 2: Install system dependencies, including the ODBC driver
FROM base AS system-deps
# Install build-essential tools and driver dependencies
RUN apt-get update && apt-get install -y curl gnupg build-essential
# Add Microsoft GPG key and repository for the ODBC driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl -fsSL "https://packages.microsoft.com/config/ubuntu/22.04/prod.list" > /etc/apt/sources.list.d/mssql-release.list
# Install the ODBC driver and required development headers
RUN apt-get update && \
    apt-get -y install unixodbc-dev && \
    ACCEPT_EULA=Y apt-get -y install msodbcsql17
# Clean up apt cache to keep image size down
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Stage 3: Install Python dependencies
FROM system-deps AS python-deps
# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .
# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 4: Production image with application code
FROM python-deps AS production
# Copy the application source code from the 'src' directory into the container's working directory
COPY ./chart_analyzer/src .
# Expose the port the app runs on
EXPOSE 8000
# Define the command to run the application
# Uvicorn will look for the 'app' object in the 'main.py' file at the root of our WORKDIR
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]