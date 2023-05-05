FROM dclong/python
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
RUN apt-get update -y \
    && apt-get install -y \
        qtbase5-dev qt5-qmake libqt5webkit5-dev build-essential xvfb libxcb-xinerama0 \
    && apt-get autoremove \
    && apt-get autoclean 
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py