-- Lists all cities in the database.

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.state_id
ORDER BY cities.id ASC
