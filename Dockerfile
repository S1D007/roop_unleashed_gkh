# Use the official Python image as base
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

RUN apt-get update
RUN apt-get install libsm6 ffmpeg libxext6 -y

COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 7860 to the outside world
EXPOSE 7860

# Define the command to run the application
CMD ["python3", "run.py"]
