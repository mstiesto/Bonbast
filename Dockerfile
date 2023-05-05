FROM python:3.10.10
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
RUN apt-get update && apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py