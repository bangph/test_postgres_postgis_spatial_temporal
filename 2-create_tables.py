import config

# temporal tables

def create_time_table_with_non_index():
    query = """
    CREATE TABLE test_time
(
  coverage_id character varying(255) NOT NULL,
  start_time timestamp(0) without time zone,
  end_time timestamp without time zone,
  CONSTRAINT test_time_pkey PRIMARY KEY (coverage_id)
);
    """
    config.run_sql(query)

def create_time_table_with_index():
    query = """
    CREATE TABLE test_time_index
(
  coverage_id character varying(255) NOT NULL,
  start_time timestamp without time zone,
  end_time timestamp without time zone,
  CONSTRAINT test_time_index_pkey PRIMARY KEY (coverage_id)
);


-- Index: index_end_time

-- DROP INDEX index_end_time;

CREATE INDEX index_end_time
  ON test_time_index
  USING btree
  (end_time);

-- Index: index_start_time

-- DROP INDEX index_start_time;

CREATE INDEX index_start_time
  ON test_time_index
  USING btree
  (start_time);"""

    config.run_sql(query)

create_time_table_with_index()

# spatial tables

def create_spatial_table_with_non_index():
    query = """
    CREATE TABLE test_bbox
(
  coverage_id character varying(255) NOT NULL,
  bbox geography,
  CONSTRAINT test_bbox_pkey PRIMARY KEY (coverage_id)
);
    """
    config.run_sql(query)

def create_spatial_table_with_index():
    query = """
    CREATE TABLE test_bbox_index
(
  coverage_id character varying(255) NOT NULL,
  bbox geography,
  CONSTRAINT test_bbox_index_pkey PRIMARY KEY (coverage_id)
);

-- Index: bbox_index

-- DROP INDEX bbox_index;

CREATE INDEX bbox_index
  ON test_bbox_index
  USING gist
  (bbox);
    """

    config.run_sql(query)


create_time_table_with_non_index()
create_time_table_with_index()

create_spatial_table_with_index()
create_spatial_table_with_non_index()

print("Created temporal and spatial tables")
