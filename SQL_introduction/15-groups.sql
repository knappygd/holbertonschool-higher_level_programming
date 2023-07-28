-- Lists the number of recordsa with the same score in the table second_table.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC
