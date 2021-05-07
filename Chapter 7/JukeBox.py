
class Jukebox:
    pass


class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.duration = duration
        self.artist = artist

    def print(self):
        sep = '_____________________'
        print(f'{self.name:<20}  {sep:>8}  {self.duration:>5}')
        print('Artist: ' + self.artist.name)
        print()


class Artist:
    def __init__(self, name):
        self.name = name


class PlayList:
    def __init__(self, name):
        self.name = name
        self.list_songs = []

    def print(self):
        for song in self.list_songs:
            song.print()

    def add_song(self, song):
        song.artist = artist
        self.list_songs.append(song)

    def play(self):
        print(self.name)
        for song in self.list_songs:
            print('Playing song ... ')
            song.print()
            answer = input("Skip song? (Yes): ").lower()
            if answer == 'yes':
                continue
        print('Playlist: ' + self.name + 'is empty. Please add more songs.')


artist = Artist('Eminem')
song_1 = Song('Stan', artist, '6:32')
song_2 = Song('Love the way you lie', artist, '4:39')
song_3 = Song('Without me', artist, '5:17')
song_4 = Song('Slim Shady', artist, '3:21')

play_list = PlayList('Eminem Playlist')
play_list.add_song(song_1)
play_list.add_song(song_2)
play_list.add_song(song_3)
play_list.add_song(song_4)
play_list.print()
print()
play_list.play()