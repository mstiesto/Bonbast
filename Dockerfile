FROM python:3.10.10-alpine
WORKDIR /app
ARG BOT_TOKEN
COPY . .
CMD python bot.py