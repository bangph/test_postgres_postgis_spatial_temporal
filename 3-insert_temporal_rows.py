import config

def insert_temporal_rows_to_non_indexed_table(values_str):
    query = """INSERT INTO test_time(coverage_id, start_time, end_time)
VALUES {}
""".format(values_str)
    config.run_sql(query)

def insert_temporal_rows_to_indexed_table(values_str):
    query = """INSERT INTO test_time_index(coverage_id, start_time, end_time)
VALUES {}
""".format(values_str)
    config.run_sql(query)


values_str = ''
min_value = 1
max_value = 1000000
for i in range(min_value, max_value):
    coverage_id = "coverage_" + str(i)
    value = """('{}', '""2012-12-01T20:07:00.589Z""', '""2012-12-09T20:47:12.500Z""')""".format(coverage_id)
    values_str += value
    if i < max_value - 1:
        values_str += ", "

print("Inserting data to non-indexed temporal table")
insert_temporal_rows_to_non_indexed_table(values_str)

print("Inserting data to indexed temporal table")
insert_temporal_rows_to_indexed_table(values_str)

