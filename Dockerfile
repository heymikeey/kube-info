FROM python:3.9-slim

WORKDIR /app

COPY ./app.py /app

RUN pip install Flask

# Set the version as an environment variable
ENV IMAGE_VERSION=$VERSION

EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

