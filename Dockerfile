
# Use the Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "app.py"]
