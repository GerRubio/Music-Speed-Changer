import csv

class Song:
    def __init__(self, track, artist, genre, bpm, energy, danceability, length):
        self.track = track
        self.artist = artist
        self.genre = genre
        self. bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self):
        return f'''Information about headers in datafile:
            0: Track name: {self.track}
            1: Artist: {self.artist}
            2: Genre: {self.genre}
            3: BPM: {self.bpm}
            4: Energy: {self.energy}
            5: Danceability: {self.danceability}
            6: Length: {self.length}
            '''

    def change_speed(self, relative_bpm):         
        pass

    @staticmethod
    def load_songs(path):
        songs = []
        
        with open(path) as f:
            reader = csv.reader(f)
            
            for row in reader:
                song = Song(*row)
                songs.append(song)
                
        return songs
    
    @staticmethod
    def save_songs(path, songs):
        with open(path, 'w') as f:
            for section in songs:
                f.write(f'{section} \n')