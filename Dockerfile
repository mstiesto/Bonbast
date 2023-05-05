FROM dclong/python
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
RUN apt-get update -y \
    && apt-get install -y \
        chromium \
    && apt-get autoremove \
    && apt-get autoclean 
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py