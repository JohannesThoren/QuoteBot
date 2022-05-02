FROM python:3.10
ADD bot.py .
ADD db.py .
RUN pip3 install nextcord psycopg2-binary dotenv
CMD ["python3", "bot.py"]