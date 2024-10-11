SELECT * FROM songs GROUP BY genre;

SELECT genre, count(*) AS count FROM songs GROUP BY genre;