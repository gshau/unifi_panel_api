FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

EXPOSE 5000
CMD [ "flask", "run",  "--host", "0.0.0.0"]