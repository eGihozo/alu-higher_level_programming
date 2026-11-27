-- Lists all records of second_table with a score >= 10.
-- Get the score and the name, best score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
