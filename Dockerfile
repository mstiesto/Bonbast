FROM python:3.10.10-alpine
WORKDIR /app
ARG BOT_TOKEN
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py