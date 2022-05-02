import os

import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
try:
    connection = psycopg2.connect(f"host={os.getenv('DATABASE_HOST')} dbname={os.getenv('DATABASE_NAME')} user={os.getenv('DATABASE_USER')} password={os.getenv('DATABASE_PASS')}")
    # Create a cursor to perform database operations
    cursor = connection.cursor()

    try:
        cursor.execute("rollback")
        connection.commit()
        cursor.execute("CREATE TABLE quotes (quote TEXT, person TEXT, year TEXT)")
        connection.commit()
    except:
        cursor.execute("rollback")
        connection.commit()
        print("table already exists")

    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")



except (Exception, Error) as error:
    print(error)

def get_quotes_from_person(person):
    cursor.execute("ROLLBACK")
    connection.commit()
    cursor.execute(f"SELECT * FROM quotes WHERE person = '{person.lower()}'")
    return cursor.fetchall()

def add_quote_to_db(quote, person, year):
    cursor.execute("ROLLBACK")
    connection.commit()
    cursor.execute("""INSERT INTO quotes (quote, person, year) VALUES (%s, %s, %s)""", (quote, person, year))
    connection.commit()
