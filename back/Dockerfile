# syntax=docker/dockerfile:1
FROM python:3.9

COPY ./app /app/app
COPY ./requirements.txt /app
COPY ./main.py /app

# 
WORKDIR /app
# 
# RUN apt-get update && \
#       apt-get -y install sudo
# # 
# RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# USER docker
# RUN sudo usermod -aG docker $(whoami)



RUN pip install -r requirements.txt

RUN apt update
RUN apt install graphviz
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80","--reload"]
