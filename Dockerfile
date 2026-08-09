# Dockerfile

FROM python:3.11

SHELL ["/bin/bash", "-c"]

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV IN_DOCKER=1

# Install system packages
RUN apt-get update && \
    apt-get install -y curl git nginx ca-certificates && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /tcd

# Copy project files
COPY . /tcd/

# Configure Git
RUN git config --global url."https://".insteadOf git://

# Install Python dependencies
RUN pip install --no-cache-dir "pipenv==2022.1.8" && \
    pipenv install --system

# Install Node dependencies
RUN npm ci --only=production

# Build frontend
RUN npm run build

# Collect static files
RUN python ./tabbycat/manage.py collectstatic --noinput -v 0

CMD sh -c 'python ./tabbycat/manage.py migrate && python ./tabbycat/manage.py runserver 0.0.0.0:$PORT'
