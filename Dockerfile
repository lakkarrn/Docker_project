# Use a lightweight Python base image
FROM python:3.9-alpine

# Create the directory inside the container
RUN mkdir -p /home/data

RUN mkdir -p /home/data/output

# Set the working directory
WORKDIR /home/data

# Copy the text files and Python script into the container
COPY IF.txt AlwaysRememberUsThisWay.txt scripts.py /home/data/

# Run the Python script
CMD ["python", "/home/data/scripts.py"]
