FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app


ADD requirements.txt /app
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 80 available to the world outside this container
EXPOSE 80

CMD python -u <MAIN_FILE_HERE>
