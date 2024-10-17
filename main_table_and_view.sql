%sql
-- Create the main table
CREATE TABLE IF NOT EXISTS default.main_table (
    id INT,
    name STRING,
    value INT
);

-- Create a view
CREATE OR REPLACE VIEW main_view AS
SELECT * FROM default.main_table;