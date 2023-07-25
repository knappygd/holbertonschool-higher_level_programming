-- Lists all the ciies of California that can be found on the database.

SELECT id, name 
FROM cities
WHERE id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC
