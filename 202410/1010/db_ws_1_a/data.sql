CREATE TABLE songs (
  id INTEGER PRIMARY KEY autoincrement,
  title TEXT,
  artists TEXT,
  album TEXT,
  genre TEXT,
  duration INTEGER
);

INSERT INTO songs (title, artists, album, genre, duration)
VALUES ('song1', 'artist1', 'album1', 'hiphop', 200);

INSERT INTO songs (title, artists, album, genre, duration)
VALUES ('song2', 'artist2', 'album2', 'ballad', 300),
  ('song3', 'artist3', 'album3', 'rock', 400),
  ('song4', 'artist4', 'album4', 'k-pop', 500),
  ('song5', 'artist5', 'album5', 'OST', 600);

UPDATE songs SET title = 'new_title' WHERE id = 1;