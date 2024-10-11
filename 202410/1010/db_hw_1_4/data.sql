SELECT * FROM tracks WHERE Name LIKE '%love';

SELECT * FROM tracks WHERE GenreId = 1 AND Milliseconds >= 300000 ORDER BY UnitPrice DESC;

SELECT GenreId, COUNT(*) AS TotalTracks FROM tracks GROUP BY GenreId;

SELECT GenreID, sum(unitprice) as TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice >= 100;