# download and install base image
FROM python:3.9.6-alpine
# setup environment variable  
ENV appHOME=/usr/src/soapdish_website_Django_Python  
# set work directory  
RUN mkdir -p $appHOME  
# where your code lives  
WORKDIR $appHOME
# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
# 
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# run this command to install all dependencies
RUN pip install --upgrade pip
# copy the project dependencies into the container working directory
COPY ./requirements.txt $appHOME  
# 
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY ./entrypoint.sh $appHOME
# RUN sed -i 's/\r$//g' /usr/src/soapdish_website_Django_Python/entrypoint.sh
RUN sed -i 's/\r$//' /usr/src/soapdish_website_Django_Python/entrypoint.sh
# 
RUN chmod +x /usr/src/soapdish_website_Django_Python/entrypoint.sh
# copy whole project to your docker home directory
COPY . $appHOME

ENTRYPOINT ["/usr/src/soapdish_website_Django_Python/entrypoint.sh"]