FROM python:latest
RUN pip3 install nextcord psycopg2-binary dotenv
CMD ["python3", "bot.py"]