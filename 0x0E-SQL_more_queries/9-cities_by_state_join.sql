-- lists all cities contained in the database hbtn_0d_usa
-- display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id
-- only one SELECT statement
SELECT *
FROM cities
RIGHT JOIN states
ON state.id = cities.states_id
ORDER BY cities.id ASC
