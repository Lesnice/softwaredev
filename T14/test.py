# Define the Album class
class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs
    
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Function to create an Album object
def create_album(album_name, album_artist, number_of_songs):
    return Album(album_name, album_artist, number_of_songs)

# Function to add an Album object to the albums list
def add_album(album_list, album):
    album_list.append(album)

# Function to print out the albums list
def print_albums(album_list):
    for idx, album in enumerate(album_list, start=1):
        print(f"Album {idx}: {album.album_name} by {album.album_artist} - {album.number_of_songs} songs")

# List to store Album objects
albums1 = []

# Add albums to the albums list
add_album(albums1, create_album("Album 1", "Artist 1", 10))
add_album(albums1, create_album("Album 2", "Artist 2", 12))
add_album(albums1, create_album("Album 3", "Artist 3", 8))
add_album(albums1, create_album("Album 4", "Artist 4", 15))
add_album(albums1, create_album("Album 5", "Artist 5", 9))

# Sort the albums list by number of songs
albums1_sorted = sorted(albums1, key=lambda x: x.number_of_songs, DESC=True)

# Print the sorted list of albums
print_albums(albums1_sorted)
