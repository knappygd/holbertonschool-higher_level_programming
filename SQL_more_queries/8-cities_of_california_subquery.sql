-- Lists all the ciies of California that can be found on the database.

SELECT id, name 
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC
