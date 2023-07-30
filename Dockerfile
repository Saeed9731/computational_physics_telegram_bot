    # Set base image
    FROM python:3.9

    # Set working directory in container
    WORKDIR /app

    # Install required packages
    COPY ./requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy project files to container
    COPY . .

    # Set default command to run the app
    CMD ["python", "app.py"]