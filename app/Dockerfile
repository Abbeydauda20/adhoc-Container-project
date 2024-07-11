# # your code goes here ...
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application source code
COPY src/ .

# Set environment variables
ENV FLASK_APP=app.py

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app" "--timeout", "120", "app:app"]



##############################################################################################

# FROM python:3.9-alpine

# # Set working directory
# WORKDIR /app

# # Copy requirements file and install dependencies
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# # Copy application source code
# COPY src/ .

# # Set environment variables
# ENV FLASK_APP=app.py

# # Run the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]


