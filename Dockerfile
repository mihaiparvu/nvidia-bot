FROM ubuntu:18.04

# install chromium
RUN  apt-get update \
  && apt-get install -yqq chromium-browser

# install chromedriver
RUN apt-get install -yqq unzip wget
RUN wget https://github.com/electron/electron/releases/download/v10.1.2/chromedriver-v10.1.2-linux-armv7l.zip
RUN unzip *.zip chromedriver -d /usr/local/bin/

# install pip
RUN apt-get install -yqq python3-pip
RUN pip3 install requests click selenium furl

WORKDIR /home

CMD ["python3", "-u", "app.py", "nvidia", "--gpu", "3080", "--locale", "de_de"]
