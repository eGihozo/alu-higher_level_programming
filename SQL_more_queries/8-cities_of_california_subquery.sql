-- Lists all the cities of California in the database hbtn_0d_usa.
-- Use a subquery to find the id of California, sorted by cities.id
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
