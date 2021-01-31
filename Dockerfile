# pull official base image
FROM python:3.9 AS base_image

RUN cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key
RUN sh -c "echo 'deb http://nginx.org/packages/mainline/debian buster nginx' > /etc/apt/sources.list.d/nginx.list"
RUN sh -c "curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -"

RUN apt-get update && \
    apt-get install -y \
    nginx libgl1-mesa-glx

FROM base_image as cool_project

# set work directory
WORKDIR /usr/src/app
COPY . .
# install dependencies
RUN python -m pip install --upgrade pip

RUN pip install -r ./requirements.txt

RUN cp ./nginx.conf /etc/nginx/conf.d/cool_project.conf

CMD ["bash", "./dockerstart.sh"]

# copy project
