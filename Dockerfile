# Use Alpine 3.14 as the base image
FROM alpine:3.14

# Update the system and install Python3, pip, and MySQL client
RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 py3-pip && \
    pip install --upgrade pip

# Copy the requirements.txt file into the image
COPY requirements.txt /tmp/

# Install the Python dependencies listed in requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY test_api.py /usr/src/app/

# Copy the main.py script into the image
COPY main.py /usr/src/app/

# Set the working directory
WORKDIR /usr/src/app

# Execute Unit Tests
RUN python3 -m unittest test_api.py

# Set the entrypoint to main.py script using Python3
ENTRYPOINT ["python3", "main.py"]

