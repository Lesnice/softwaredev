"""
Design a class Album which should contain:
data fields album_name(str), number_of_songs(int)
and album_artist(str)"""
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
#albums1_sorted = sorted(albums1, key=lambda x: x.number_of_songs)

def display_albums(albums):
    
    """ 
    Argument: The chosen album to display ablums1 or albums2
    Return: Displays the content of the chosen album

    """
    for album in albums:
        print(album)
        
# Print the sorted list of albums


def sort_number_songs(albums):
    """ 
    Argument: Chosen album to sort by number of songs
    Return: Sorts the chosen album by number of songs
    """
    albums.sort(key=lambda album:album.number_of_songs)
    #print sorted albums1 list
    print("\nAlbum sorted by number of songs in ascending order:")
    display_albums(albums)
    
sort_number_songs(albums1)

#list for  5 instances

albums2 = []

#add 5 additional instances of album list
add_album(albums2, create_album("Album 6", "Artist 6", 10))
add_album(albums2, create_album("Album 7", "Artist 7", 16))
add_album(albums2, create_album("Album 8", "Artist 8", 81))
add_album(albums2, create_album("Album 9", "Artist 9", 1))
add_album(albums2, create_album("Album 10", "Artist 10", 7))

def swap_position(album, position1, position2):
    """ 
    Argument: chosen album to swap elements, and the position to swap
    Return: swaps the elements at the given position"""
    album[position1 -1], album[position2 -1] = album[position2 -1], album[position1 -1]
    print(f"\nAlbum post swapping {position1} for {position2}")
    display_albums(albums1)
    
    
swap_position(albums1, 1, 2)

def find_index(albums, album_name):
    """ 
    Argument: chosen album to search and album name to search for
    Return: index of the album nae in the chosen album"""
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            print(f"\nIndex of '{album_name}':{index}")
            

albums2.extend(albums1)  #copy all the albums from albums1 into albums and display it
print("\nAlbum 2 after copying Album 1 into it: ")

albums2.extend([
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!...I Did It Again", "Britney Spears", 16)
])

find_index(albums2, "Dark Side of the Moon")#Displays the index 