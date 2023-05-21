FROM python:latest

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

# setup environment variable  
ENV appHOME=/home/webApps  

# set work directory  
RUN mkdir -p $appHOME  

# where your code lives  
WORKDIR $appHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Set up and activate virtual environment
# ENV VIRTUAL_ENV "/venv"
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# install dependencies  
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $appHOME

# run this command to install all dependencies  
# RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
