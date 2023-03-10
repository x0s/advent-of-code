FROM python:3.11-slim-buster

# Install make
RUN apt-get update && \
    apt-get -y install make && \
    apt-get -y install git

RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Install the package
COPY ./pyproject.toml /app
RUN python -m pip install .

ENV PYTHONPATH /app

# Copy scripts to the app folder
COPY . /app

# Start by showing the command menu (equivalent of "make help")
CMD ["make"]