FROM dclong/python
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
RUN apt-get update -y \
    && apt-get install -y \
    wget xvfb unzip chromium-browser \
    && apt-get autoremove \
    && apt-get autoclean
ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /usr/bin/
RUN wget -q --continue -P . "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip ./chromedriver* -d $CHROMEDRIVER_DIR
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py