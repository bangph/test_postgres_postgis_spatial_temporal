import psycopg2


def insert_vendor(values_str):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO test_bbox_index(coverage_id, bbox)
VALUES {}
""".format(values_str)
    conn = None
    vendor_id = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="localhost", database="petascopedb_enterprise_polygon", user="postgres", password="postgres")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

values_str = ''
min_value = 1
max_value = 1000000
for i in range(min_value, max_value):
    print("Insert column: " + str(i))
    coverage_id = "coverage_" + str(i)
    value = """('{}', ST_GeomFromText('POLYGON((156.4750000 -8.9750000, 156.4750000 -44.4750000, 111.9750000 -44.4750000, 111.9750000 -8.9750000, 156.4750000 -8.9750000))', 4326))""".format(coverage_id)
    values_str += value
    if i < max_value - 1:
        values_str += ", "

insert_vendor(values_str)
