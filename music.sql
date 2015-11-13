DROP TABLE IF EXISTS artists;
CREATE TABLE artists (
    id int PRIMARY KEY,
    artist varchar NOT NULL
);

DROP TABLE IF EXISTS album;
CREATE TABLE album (
    album_id int PRIMARY KEY,
    artist_id int NOT NULL
    FOREIGN KEY (artist_id)
        REFERENCES artist(id)
    album_title varchar NOT NULL
);

DROP TABLE IF EXISTS song;
CREATE TABLE song (
    song_id int PRIMARY KEY,
    song varchar NOT NULL,
    album_id int NOT NULL
    FOREIGN KEY (album_id)
        REFERENCES albums(album_id),
    artist_id int NOT NULL
    FOREIGN KEY (artist_id)
        REFERENCES artists(id),
    track_num int NOT NULL,
    track_time varchar
);
