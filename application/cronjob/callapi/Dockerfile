FROM python:3.9-slim

WORKDIR /app

# Copy the script and requirements file to the container
COPY call.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "call.py"]
