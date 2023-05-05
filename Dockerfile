FROM dclong/python
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
RUN apt-get update -y \
    && apt-get install -y \
        qt5-default libqt5webkit5-dev build-essential xvfb \
    && apt-get autoremove \
    && apt-get autoclean 
RUN pip3 install -r requirements.txt
COPY bot.py .
CMD python bot.py