
FROM ubuntu:18.04

# install chromium
RUN  apt-get update \
  && apt-get install -yqq chromium-browser

# install chromedriver
RUN apt-get install -yqq unzip wget
RUN wget https://github.com/electron/electron/releases/download/v9.0.0-beta.15/chromedriver-v9.0.0-beta.15-linux-armv7l.zip
RUN unzip *.zip chromedriver -d /usr/local/bin/

# install pip
RUN apt-get install -yqq python3-pip
RUN pip3 install requests click selenium furl questionary spinlog

WORKDIR /home

CMD ["python3", "-u", "app.py", "nvidia", "--gpu", "3080", "--locale", "de_de"]
