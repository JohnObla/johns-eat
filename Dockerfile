# Current version of Ubunutu's python
FROM python:3.8.2

# Generic python environment setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creates work directory called 'code'
WORKDIR /code

# Copies requirements.txt containing pip dependencies
COPY requirements.txt .

# Install dependencies via 'requirements.txt', then creates a user that matches user id of my host login - this avoids permission errors on host
RUN pip install --requirement requirements.txt && \
    groupadd code_executor_group && \
    useradd code_executor_user --gid code_executor_group --uid 1000

# Switches to created user
USER code_executor_user

# Copies files over to the image
COPY . .