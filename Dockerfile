FROM python:3.10.10
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py