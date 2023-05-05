FROM mcr.microsoft.com/playwright
WORKDIR /app
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN
COPY . .
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
CMD python bot.py