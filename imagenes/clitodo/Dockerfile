FROM python:3.9.19-slim-bullseye
WORKDIR /app
COPY instalaciones.txt instalaciones.txt
RUN echo "alias todos='python /app/main.py'" >> ~/.bashrc && pip3 install -r instalaciones.txt
COPY . .