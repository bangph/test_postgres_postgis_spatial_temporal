import psycopg2

username = "postgres"
password = "postgres"
database = "test_spatial_temporal"


def run_sql(query, input_database=None):
    if input_database is None:
        input_database = database

    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="localhost", database=input_database, user=username, password=password)
        conn.autocommit = True
        # create a new cursor
        cur = conn.cursor()
        cur.execute(query)
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def run_sql_with_output(query, input_database=None):
    if input_database is None:
        input_database = database

    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="localhost", database=input_database, user=username, password=password)
        conn.autocommit = True
        # create a new cursor
        cur = conn.cursor()
        cur.execute(query)

        results = cur.fetchall()
        for x in results:
            print(x)

        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
