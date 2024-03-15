-- lists all cities contained in the database hbtn_0d_usa
-- display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id
-- only one SELECT statement
SELECT *
FROM cities
FULL JOIN state
ON cities.state_id = states.id
WHERE cities.state_id IS NULL OR states.id IS NULL
