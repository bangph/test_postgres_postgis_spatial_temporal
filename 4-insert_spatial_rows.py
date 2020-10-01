import config

def insert_spatial_rows_to_non_indexed_table(values_str):
    query = """INSERT INTO test_bbox(coverage_id, bbox) VALUES {}""".format(values_str)
    config.run_sql(query)

def insert_spatial_rows_to_indexed_table(values_str):
    query = """INSERT INTO test_bbox_index(coverage_id, bbox) VALUES {}""".format(values_str)
    config.run_sql(query)

values_str = ''
min_value = 1
max_value = 1000000
for i in range(min_value, max_value):
    coverage_id = "coverage_" + str(i)
    value = """('{}', ST_GeomFromText('POLYGON((156.4750000 -8.9750000, 156.4750000 -44.4750000, 111.9750000 -44.4750000, 111.9750000 -8.9750000, 156.4750000 -8.9750000))', 4326))""".format(coverage_id)
    values_str += value
    if i < max_value - 1:
        values_str += ", "

print("Inserting data to non-indexed spatial table")
insert_spatial_rows_to_non_indexed_table(values_str)

print("Inserting data to indexed spatial table")
insert_spatial_rows_to_indexed_table(values_str)
