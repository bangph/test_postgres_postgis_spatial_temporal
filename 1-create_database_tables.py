import psycopg2
import config


def create_database():
    query = """CREATE DATABASE {};""".format(config.database)
    config.run_sql(query, "postgres")

def create_postgis_extension():
    query = """ CREATE EXTENSION postgis """
    config.run_sql(query)

create_database()
create_postgis_extension()

print("Created database: " + config.database)
