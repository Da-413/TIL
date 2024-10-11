SELECT * FROM artists;

SELECT count(*) FROM artists;

SELECT * FROM artists WHERE Name = 'AC/DC';

SELECT artistid, name from artists;

SELECT * FROM artists WHERE name = 'Gilberto Gil' OR name = 'Ed Motta';

SELECT * FROM artists ORDER BY Name DESC;

SELECT * FROM artists WHERE Name LIKE 'Vinícius%' LIMIT 2;

SELECT ArtistId FROM artists WHERE ArtistId >= 50 and ArtistId <= 70;