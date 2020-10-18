import sys

from spotify import Song

'''Information about headers in datafile
0: Track name
1: Artist name
2: Genre
3: Beats per minute
4: Energy
5: Danceability
6: Length'''

if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(sys.argv[1])  # Read keyboard input

    # Load songs (from input_file)

    # Change speed of all songs

    # Save songs (to output_file)