CREATE TABLE singer ( id SERIAL PRIMARY KEY, name VARCHAR(50));

CREATE TABLE song ( id INTEGER PRIMARY KEY, name VARCHAR(50), singer_id INTEGER, FOREIGN KEY(singer_id) REFERENCES singer(id) ON DELETE CASCADE);

INSERT INTO singer (id, name) VALUES (1, 'Nicki Minaj'), (2, 'Lady Gaga'), (3, 'Taylor Swift'), (4, 'Tom Jones');

INSERT INTO song (id, name, singer_id) VALUES (1, 'Anaconda', 1), (2, 'Paparazzi', 2), (3, 'Bad Romance', 2), (4, 'Sex Bomb', 4);


