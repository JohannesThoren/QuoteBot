FROM python:3.10
ADD bot.py .
ADD db.py .
RUN pip install nextcord psycopg2-binary python-dotenv
CMD ["python3", "bot.py"]