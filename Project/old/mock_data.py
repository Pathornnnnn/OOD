from Backend.player import HybridMusicPlayer
from Backend.models import Artist, Album, Song
player = HybridMusicPlayer()


def init_data():
    # Artist 1: Timethai
    artist1 = Artist(1, "Timethai")
    artist1.add_url("https://yt3.googleusercontent.com/tHRne6pvXT_dSlmZ2riiV418PkxS7ITXR5jTg89nqUnsLgyxeiULk62eacNj4THqh9_jXoYg=s900-c-k-c0x00ffffff-no-rj")

    album1 = Album(1, "Thaisoul")
    album1.add_url("https://example.com/thaisoul.jpg")
    song1 = Song(1, "No More Tears", 210)
    song1.add_url("https://example.com/no_more_tears.mp3")
    song2 = Song(2, "Playground", 200)
    song2.add_url("https://example.com/playground.mp3")
    album1.add_song(song1)
    album1.add_song(song2)
    artist1.add_album(album1)

    album1b = Album(4, "Time 2 Shine")
    album1b.add_url("https://example.com/time2shine.jpg")
    song7 = Song(7, "Shining Star", 220)
    song7.add_url("https://example.com/shining_star.mp3")
    song8 = Song(8, "Feel Alive", 205)
    song8.add_url("https://example.com/feel_alive.mp3")
    album1b.add_song(song7)
    album1b.add_song(song8)
    artist1.add_album(album1b)

    album1c = Album(5, "Timethai Unplugged")
    album1c.add_url("https://example.com/timethai_unplugged.jpg")
    song9 = Song(9, "Relax & Flow", 230)
    song9.add_url("https://example.com/relax_flow.mp3")
    song10 = Song(10, "Chill Night", 240)
    song10.add_url("https://example.com/chill_night.mp3")
    artist1.add_album(album1c)

    # Artist 2: URBOYTJ
    artist2 = Artist(2, "URBOYTJ")
    artist2.add_url("https://cms.dmpcdn.com/musicarticle/2022/06/25/fb6dc850-f436-11ec-ae6f-a5bdea68cb38_original.jpg")

    album2 = Album(2, "Selfmade")
    album2.add_url("https://example.com/selfmade.jpg")
    song3 = Song(3, "Do You Mind?", 240)
    song3.add_url("https://example.com/do_you_mind.mp3")
    song4 = Song(4, "Rebound", 230)
    song4.add_url("https://example.com/rebound.mp3")
    album2.add_song(song3)
    album2.add_song(song4)
    artist2.add_album(album2)

    album2b = Album(6, "Why Not?")
    album2b.add_url("https://example.com/why_not.jpg")
    song11 = Song(11, "Why Tho ?", 215)
    song11.add_url("https://example.com/why_tho.mp3")
    song12 = Song(12, "Fast Life", 225)
    song12.add_url("https://example.com/fast_life.mp3")
    album2b.add_song(song11)
    album2b.add_song(song12)
    artist2.add_album(album2b)

    # Artist 3: F.HERO
    artist3 = Artist(3, "F.HERO")
    artist3.add_url("https://i.scdn.co/image/ab6761610000e5ebcf6dc7909f08fd4c42c59a24")

    album3 = Album(3, "Into the New Era")
    album3.add_url("https://i.scdn.co/image/ab67616d0000b2738b7c0a913dbea38a0626bd10")
    song5 = Song(5, "Do You", 260)
    song5.add_url("https://musicstation.kapook.com/files_music2008/picture/4/21720.jpg")
    song6 = Song(6, "a better tomorrow", 275)
    song6.add_url("https://i.ytimg.com/vi/W4WCu1k9p4k/sddefault.jpg")
    album3.add_song(song5)
    album3.add_song(song6)
    artist3.add_album(album3)

    album3b = Album(7, "Collab Hits")
    album3b.add_url("https://example.com/collab_hits.jpg")
    song13 = Song(13, "Epic Flow ft. Lazyloxy", 250)
    song13.add_url("https://example.com/epic_flow_lazyloxy.mp3")
    song14 = Song(14, "Street Anthem", 245)
    song14.add_url("https://example.com/street_anthem.mp3")
    album3b.add_song(song13)
    album3b.add_song(song14)
    artist3.add_album(album3b)  

    player.add_artist(artist1) 
    player.add_artist(artist2)
    player.add_artist(artist3)
    print("Initialized mock data with 3 artists, 7 albums, and 14 songs.")