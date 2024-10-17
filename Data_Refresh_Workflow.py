# Databricks notebook source
# MAGIC %md
# MAGIC Cell 1: Generate Fake Data and Create Staging Table:
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create the staging table
# MAGIC      CREATE TABLE IF NOT EXISTS staging_table (
# MAGIC          id INT,
# MAGIC          name STRING,
# MAGIC          value INT
# MAGIC      );
# MAGIC
# MAGIC      -- Insert fake data into the staging table
# MAGIC      INSERT INTO staging_table (id, name, value)
# MAGIC      VALUES
# MAGIC      (1, 'Name_1', 10),
# MAGIC      (2, 'Name_2', 20),
# MAGIC      (3, 'Name_3', 30),
# MAGIC      (4, 'Name_4', 40),
# MAGIC      (5, 'Name_5', 50),
# MAGIC      (6, 'Name_6', 60),
# MAGIC      (7, 'Name_7', 70),
# MAGIC      (8, 'Name_8', 80),
# MAGIC      (9, 'Name_9', 90),
# MAGIC      (10, 'Name_10', 100);

# COMMAND ----------

# MAGIC %md
# MAGIC Cell 2: Create Main Table and View:
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create the main table
# MAGIC      CREATE TABLE IF NOT EXISTS main_table (
# MAGIC          id INT,
# MAGIC          name STRING,
# MAGIC          value INT
# MAGIC      );
# MAGIC
# MAGIC      -- Create a view
# MAGIC      CREATE OR REPLACE VIEW main_view AS
# MAGIC      SELECT * FROM main_table;

# COMMAND ----------

# MAGIC %md
# MAGIC Cell 3: Automate Drop and Refresh Process:
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Drop the main table if it exists
# MAGIC      DROP TABLE IF EXISTS main_table;
# MAGIC
# MAGIC      -- Create the main table from the staging table
# MAGIC      CREATE TABLE main_table AS
# MAGIC      SELECT * FROM staging_table;
# MAGIC
# MAGIC      -- Refresh the view
# MAGIC      CREATE OR REPLACE VIEW main_view AS
# MAGIC      SELECT * FROM main_table;
# MAGIC
# MAGIC -- # # Define the SQL commands
# MAGIC -- #      drop_main_table_sql = "DROP TABLE IF EXISTS main_table;"
# MAGIC -- #      create_main_table_sql = """
# MAGIC -- #      CREATE TABLE main_table AS
# MAGIC -- #      SELECT * FROM staging_table;
# MAGIC -- #      """
# MAGIC -- #      refresh_view_sql = "CREATE OR REPLACE VIEW main_view AS SELECT * FROM main_table;"
# MAGIC
# MAGIC -- #      # Execute the SQL commands
# MAGIC -- #      spark.sql(drop_main_table_sql)
# MAGIC -- #      spark.sql(create_main_table_sql)
# MAGIC -- #      spark.sql(refresh_view_sql)

# COMMAND ----------

# MAGIC %md
# MAGIC Cell 4: Verify the Data:
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Verify the main table
# MAGIC SELECT * FROM main_table LIMIT 10;
# MAGIC
# MAGIC -- Verify the view
# MAGIC SELECT * FROM main_view LIMIT 10;
