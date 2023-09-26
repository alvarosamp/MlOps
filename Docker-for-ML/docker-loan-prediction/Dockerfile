#base image
FROM python:3.8-slim-buster
# upgrade pip
RUN pip install --upgrade pip 

# Copiying all the files to source directory
COPY . /src

# Set working directory to previously added source directory
WORKDIR /src

# Giving permissions to python file
RUN chmod +x docker_train.py

# Install required python dependencies from requirements file
RUN pip install -r requirements.txt

# Run docker_train.py file
ENTRYPOINT ["python"]

CMD ["docker_train.py"]