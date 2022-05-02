FROM python:3.10
ADD bot.py. db.py.
RUN pip install nextcord dotenv psycopg2-binary
CMD ["python3" "bot.py"]
