from Backend.player import HybridMusicPlayer
from Backend.models import Artist, Album, Song
player = HybridMusicPlayer()
def init_data():
    """
    Initialize the music player with mock data.
    """

    # ========== Artist 1 ==========
    artist1 = Artist(1, "Ed Sheeran")
    album1 = Album(1, "Divide")
    song1 = Song(1, "Shape of You", 240)
    song2 = Song(2, "Perfect", 263)
    album1.add_song(song1)
    album1.add_song(song2)
    artist1.add_album(album1)
    player.add_artist(artist1)


    # ========== Artist 2 ==========
    artist2 = Artist(2, "Taylor Swift")
    album2 = Album(2, "1989")
    song3 = Song(3, "Blank Space", 231)
    song4 = Song(4, "Style", 230)
    album2.add_song(song3)
    album2.add_song(song4)
    artist2.add_album(album2)
    player.add_artist(artist2)


    # ========== Artist 3 ==========
    artist3 = Artist(3, "Adele")
    album3 = Album(3, "25")
    song5 = Song(5, "Hello", 295)
    song6 = Song(6, "When We Were Young", 290)
    album3.add_song(song5)
    album3.add_song(song6)
    artist3.add_album(album3)
    player.add_artist(artist3)


    # ========== Artist 4 ==========
    artist4 = Artist(4, "Bruno Mars")
    album4 = Album(4, "24K Magic")
    song7 = Song(7, "24K Magic", 227)
    song8 = Song(8, "That's What I Like", 210)
    album4.add_song(song7)
    album4.add_song(song8)
    artist4.add_album(album4)
    player.add_artist(artist4)


    # ========== Artist 5 ==========
    artist5 = Artist(5, "The Weeknd")
    album5 = Album(5, "After Hours")
    song9 = Song(9, "Blinding Lights", 200)
    song10 = Song(10, "Save Your Tears", 215)
    album5.add_song(song9)
    album5.add_song(song10)
    artist5.add_album(album5)
    player.add_artist(artist5)


    # ========== Artist 6 ==========
    artist6 = Artist(6, "Imagine Dragons")
    album6 = Album(6, "Evolve")
    song11 = Song(11, "Believer", 204)
    song12 = Song(12, "Thunder", 187)
    album6.add_song(song11)
    album6.add_song(song12)
    artist6.add_album(album6)
    player.add_artist(artist6)
