FROM dclong/python
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
WORKDIR /app
COPY bot.py requirements.txt .
RUN pip3 install -r requirements.txt
CMD python bot.py