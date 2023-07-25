-- Lists all the ciies of California that can be found on the database.

SELECT cities.name
FROM cities, states
WHERE state.name = 'California'
ORDER BY cities.id ASC
