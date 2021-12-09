-- List all records (rows) with score >= 10
-- All records (rows) must be ordered in descending score.
SELECT score, name FROM second_table WHERE SCORE >= 10 ORDER BY score DESC;
