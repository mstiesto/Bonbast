FROM python:3.10.10-alpine
ARG BOT_TOKEN
COPY . .
CMD python bot.py