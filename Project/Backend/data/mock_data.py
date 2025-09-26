from Backend.models.artist import Artist
from Backend.models.album import Album
from Backend.models.song import Song
from Backend.core.hybrid_music_player import player

def init_data():
    # -------------------------
    # Artist 1: Timethai
    # -------------------------
    artist1 = Artist(1, "Timethai", "https://yt3.googleusercontent.com/tHRne6pvXT_dSlmZ2riiV418PkxS7ITXR5jTg89nqUnsLgyxeiULk62eacNj4THqh9_jXoYg=s900-c-k-c0x00ffffff-no-rj")
    
    # Album 1
    album1 = Album(1, "Thaisoul", "https://example.com/thaisoul.jpg")
    album1.add_song(Song(1, "No More Tears", 210, "https://example.com/no_more_tears.mp3"))
    album1.add_song(Song(2, "Playground", 200, "https://example.com/playground.mp3"))
    artist1.add_album(album1)

    # Album 1b
    album1b = Album(4, "Time 2 Shine", "https://example.com/time2shine.jpg")
    album1b.add_song(Song(7, "Shining Star", 220, "https://example.com/shining_star.mp3"))
    album1b.add_song(Song(8, "Feel Alive", 205, "https://example.com/feel_alive.mp3"))
    artist1.add_album(album1b)

    # Album 1c
    album1c = Album(5, "Timethai Unplugged", "https://example.com/timethai_unplugged.jpg")
    album1c.add_song(Song(9, "Relax & Flow", 230, "https://example.com/relax_flow.mp3"))
    album1c.add_song(Song(10, "Chill Night", 240, "https://example.com/chill_night.mp3"))
    artist1.add_album(album1c)

    # -------------------------
    # Artist 2: URBOYTJ
    # -------------------------
    artist2 = Artist(2, "URBOYTJ", "https://cms.dmpcdn.com/musicarticle/...")

    album2 = Album(2, "Selfmade", "https://example.com/selfmade.jpg")
    album2.add_song(Song(3, "Do You Mind?", 240, "https://example.com/do_you_mind.mp3"))
    album2.add_song(Song(4, "Rebound", 230, "https://example.com/rebound.mp3"))
    artist2.add_album(album2)

    album2b = Album(6, "Why Not?", "https://example.com/why_not.jpg")
    album2b.add_song(Song(11, "Why Tho ?", 215, "https://example.com/why_tho.mp3"))
    album2b.add_song(Song(12, "Fast Life", 225, "https://example.com/fast_life.mp3"))
    artist2.add_album(album2b)

    # -------------------------
    # Artist 3: F.HERO
    # -------------------------
    artist3 = Artist(3, "F.HERO", "https://i.scdn.co/image/ab6761610000e5ebcf6dc7909f08fd4c42c59a24")

    album3 = Album(3, "Into the New Era", "https://i.scdn.co/image/ab67616d0000b2738b7c0a913dbea38a0626bd10")
    album3.add_song(Song(5, "Do You", 260, "https://musicstation.kapook.com/files_music2008/picture/4/21720.jpg"))
    album3.add_song(Song(6, "A Better Tomorrow", 275, "https://i.ytimg.com/vi/W4WCu1k9p4k/sddefault.jpg"))
    artist3.add_album(album3)

    album3b = Album(7, "Collab Hits", "https://example.com/collab_hits.jpg")
    album3b.add_song(Song(13, "Epic Flow ft. Lazyloxy", 250, "https://example.com/epic_flow_lazyloxy.mp3"))
    album3b.add_song(Song(14, "Street Anthem", 245, "https://example.com/street_anthem.mp3"))
    artist3.add_album(album3b)

    # -------------------------
    # Add artists to player
    # -------------------------
    player.add_artist(artist1)
    player.add_artist(artist2)
    player.add_artist(artist3)

    print("Initialized mock data with 3 artists, 7 albums, and 14 songs.")
