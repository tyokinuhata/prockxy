import sqlite3

class CacheMusics:

    def __init__(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS musics(id INTEGER PRIMARY KEY AUTOINCREMENT, song_name STRING, artist STRING)')
        self.conn.commit()
        return self

    def drop_table(self):
        self.cur.execute('DROP TABLE IF EXISTS musics')
        self.conn.commit()
        return self

    def insert(self, song_name, artist_name):
        self.cur.execute('INSERT INTO musics(song_name, artist) VALUES(?, ?)', (song_name, artist_name))
        self.conn.commit()
        return self

    def close(self):
        self.conn.close()
        return self

if __name__ == '__main__':
    cache_musics = CacheMusics()
    cache_musics.drop_table().create_table().close()
