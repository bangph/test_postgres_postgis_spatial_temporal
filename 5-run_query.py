import config

with open('input_query', 'r') as file:
    query = file.read()

config.run_sql_with_output(query)

