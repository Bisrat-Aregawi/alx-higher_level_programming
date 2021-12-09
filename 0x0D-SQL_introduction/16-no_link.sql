-- List all records of table `second_table`
-- Ignore records (rows) without name value set
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
