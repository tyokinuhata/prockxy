import sqlite3

class Musics:
    def __init__(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS musics(id INTEGER PRIMARY KEY AUTOINCREMENT, song_name STRING, artist STRING, cd_jacket STRING)')
        self.conn.commit()
        return self

    def drop_table(self):
        self.cur.execute('DROP TABLE IF EXISTS musics')
        self.conn.commit()
        return self

    def insert(self, song_name, artist_name, cd_jacket):
        self.cur.execute('INSERT INTO musics(song_name, artist, cd_jacket) VALUES(?, ?, ?)', (song_name, artist_name, cd_jacket))
        self.conn.commit()
        return self

    def find(self, id = 1):
        return self.cur.execute('SELECT * FROM musics WHERE id = ?', (str(id), )).fetchone()

    def count(self):
        return self.cur.execute('SELECT count(*) FROM musics').fetchall()[0][0]

    def exists(self, song_name, artist):
        self.cur.execute('SELECT * FROM musics WHERE EXISTS(SELECT * FROM musics WHERE song_name = ? AND artist = ?)', (song_name, artist, ))
        return True if self.cur.fetchone() else False

    def close(self):
        self.conn.close()
        return self

if __name__ == '__main__':
    print('Initializing database ...')
    musics = Musics()
    musics.drop_table().create_table().close()
    print('Succeed!')
