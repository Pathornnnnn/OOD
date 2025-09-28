# from Backend.models.artist import Artist
# from Backend.models.album import Album
# from Backend.models.song import Song
# from Backend.core.hybrid_music_player import player

# def init_data():
#     # -------------------------
#     # Artist 1: Timethai
#     # -------------------------
#     artist1 = Artist(1, "Timethai", "https://yt3.googleusercontent.com/tHRne6pvXT_dSlmZ2riiV418PkxS7ITXR5jTg89nqUnsLgyxeiULk62eacNj4THqh9_jXoYg=s900-c-k-c0x00ffffff-no-rj")
    
#     # Album 1
#     album1 = Album(1, "Thaisoul", "https://www.gqthailand.com/_next/image?url=https%3A%2F%2Ffiles.gqthailand.com%2Fuploads%2Fweb-potrai-logo-time-thai-7_2.webp&w=2048&q=75")
#     album1.add_song(Song(1, "No More Tears", 210, "https://musicstation.kapook.com/files_music2008/picture/1/7191_1408.jpg"))
#     album1.add_song(Song(2, "Playground", 200, "https://yt3.googleusercontent.com/h1OX0nziujfnO7NEQSAmvBVWVtiz3-W13xSeHuiWIT60N5PTWoaIlC1lGfg9EImNePUZ1sBl=s160-c-k-c0x00ffffff-no-rj"))
#     artist1.add_album(album1)

#     # Album 1b
#     album1b = Album(4, "Time 2 Shine", "https://example.com/time2shine.jpg")
#     album1b.add_song(Song(7, "Shining Star", 220, "https://example.com/shining_star.mp3"))
#     album1b.add_song(Song(8, "Feel Alive", 205, "https://example.com/feel_alive.mp3"))
#     artist1.add_album(album1b)

#     # Album 1c
#     album1c = Album(5, "Timethai Unplugged", "https://example.com/timethai_unplugged.jpg")
#     album1c.add_song(Song(9, "Relax & Flow", 230, "https://example.com/relax_flow.mp3"))
#     album1c.add_song(Song(10, "Chill Night", 240, "https://example.com/chill_night.mp3"))
#     artist1.add_album(album1c)

#     # -------------------------
#     # Artist 2: URBOYTJ
#     # -------------------------
#     artist2 = Artist(2, "URBOYTJ", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0BOLBObSGn6_-SPD7U3KMnsmzK5kp6Ktz4Q&s")

#     album2 = Album(2, "Selfmade", "https://example.com/selfmade.jpg")
#     album2.add_song(Song(3, "Do You Mind?", 240, "https://example.com/do_you_mind.mp3"))
#     album2.add_song(Song(4, "Rebound", 230, "https://example.com/rebound.mp3"))
#     artist2.add_album(album2)

#     album2b = Album(6, "Why Not?", "https://example.com/why_not.jpg")
#     album2b.add_song(Song(11, "Why Tho ?", 215, "https://example.com/why_tho.mp3"))
#     album2b.add_song(Song(12, "Fast Life", 225, "https://example.com/fast_life.mp3"))
#     artist2.add_album(album2b)

#     # -------------------------
#     # Artist 3: F.HERO
#     # -------------------------
#     artist3 = Artist(3, "F.HERO", "https://i.scdn.co/image/ab6761610000e5ebcf6dc7909f08fd4c42c59a24")

#     album3 = Album(3, "Into the New Era", "https://i.scdn.co/image/ab67616d0000b2738b7c0a913dbea38a0626bd10")
#     album3.add_song(Song(5, "Do You", 260, "https://musicstation.kapook.com/files_music2008/picture/4/21720.jpg"))
#     album3.add_song(Song(6, "A Better Tomorrow", 275, "https://i.ytimg.com/vi/W4WCu1k9p4k/sddefault.jpg"))
#     artist3.add_album(album3)

#     album3b = Album(7, "Collab Hits", "https://example.com/collab_hits.jpg")
#     album3b.add_song(Song(13, "Epic Flow ft. Lazyloxy", 250, "https://example.com/epic_flow_lazyloxy.mp3"))
#     album3b.add_song(Song(14, "Street Anthem", 245, "https://example.com/street_anthem.mp3"))
#     artist3.add_album(album3b)

#     # -------------------------
#     # Add artists to player
#     # -------------------------
#     player.add_artist(artist1)
#     player.add_artist(artist2)
#     player.add_artist(artist3)

#     print("Initialized mock data with 3 artists, 7 albums, and 14 songs.")

from Backend.models.artist import Artist
from Backend.models.album import Album
from Backend.models.song import Song
from Backend.core.hybrid_music_player import player

def init_data():
    # -------------------------
    # Artist 1: Drake
    # -------------------------
    # ใช้ URL จาก Wikimedia Commons ที่เป็นภาพ public domain / สาธารณะ
    artist1 = Artist(1, "Drake", "https://upload.wikimedia.org/wikipedia/commons/2/28/Drake_July_2016.jpg")
    
    # (ใส่ album / song เหมือนเดิมหรือเปลี่ยนตามต้องการ)
    album1 = Album(1, "Views", "https://upload.wikimedia.org/wikipedia/en/a/af/Drake_-_Views_cover.jpg")
    album1.add_song(Song(1, "Hotline Bling", 210, "https://i.ytimg.com/vi/uxpDa-c-4Mc/maxresdefault.jpg"))
    album1.add_song(Song(2, "One Dance", 200, "https://i1.sndcdn.com/artworks-mS6d7vFc5d7IAkIW-L8hkzg-t500x500.jpg"))
    artist1.add_album(album1)

    album1b = Album(4, "Scorpion", "https://upload.wikimedia.org/wikipedia/en/9/90/Scorpion_by_Drake.jpg")
    album1b.add_song(Song(7, "God's Plan", 220, "https://i.ytimg.com/vi/RfO1DTGwIAA/sddefault.jpg"))
    album1b.add_song(Song(8, "In My Feelings", 205, "https://i.ytimg.com/vi/suz7pWi1mOs/sddefault.jpg"))
    artist1.add_album(album1b)

    # -------------------------
    # Artist 2: Lil Uzi Vert
    # -------------------------
    artist2 = Artist(2, "Lil Uzi Vert", "https://upload.wikimedia.org/wikipedia/commons/4/44/Lil_Uzi_Vert_%282018%29.png")

    album2 = Album(2, "Luv Is Rage 2", "https://i.scdn.co/image/ab67616d0000b273f23aee9d3be9fcbca1bc6352")
    album2.add_song(Song(3, "XO Tour Llif3", 240, "https://i.ytimg.com/vi/WrsFXgQk5UI/hqdefault.jpg"))
    album2.add_song(Song(4, "The Way Life Goes", 230, "https://i.ytimg.com/vi/Vi2XaiKhgiU/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDiA1wHYBpPT2q6H2l2b0IqHTb-8g"))
    artist2.add_album(album2)

    album2b = Album(6, "Eternal Atake", "https://i.scdn.co/image/ab67616d0000b273158b08c02c249bc651b3b47a")
    album2b.add_song(Song(11, "Baby Pluto", 215, "https://i1.sndcdn.com/artworks-z9V7CpywBmXYV8Jf-BJ5PUA-t500x500.jpg"))
    album2b.add_song(Song(12, "Futsal Shuffle 2020", 225, "https://i1.sndcdn.com/artworks-1FIrnlRk17n5-0-t500x500.jpg"))
    artist2.add_album(album2b)

    # -------------------------
    # Artist 3: Jack Harlow
    # -------------------------
    # สำหรับ Jack Harlow ผมหา URL ที่มั่นใจได้น้อยกว่า — คุณอาจต้องอัปโหลดภาพหรือใช้ URL จาก server ของคุณ
    artist3 = Artist(3, "Jack Harlow", "https://yt3.googleusercontent.com/6KQV9B-m_cFu0b1aUnUFfbA3IQL5xY5yYgTWwuIEPJgY8p8HzgwtotTeksTzFQtdrJBrwd7i4A=s900-c-k-c0x00ffffff-no-rj")

    album3 = Album(3, "Thats What They All Say", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ805A5w_Nhnb4aI42h-bkiCOv8n8x1Nwx3Zg&s")
    album3.add_song(Song(5, "Whats Poppin", 260, "https://i.ytimg.com/vi/w9uWPBDHEKE/hqdefault.jpg"))
    album3.add_song(Song(6, "Tyler Herro", 275, "https://upload.wikimedia.org/wikipedia/en/4/45/Jack_Harlow_-_Tyler_Herro.png"))
    artist3.add_album(album3)

    album3b = Album(7, "Come Home the Kids Miss You", "https://i.scdn.co/image/ab67616d0000b2738e55edb69ca44a25b52b17bb")
    album3b.add_song(Song(13, "First Class", 250, "https://i.ytimg.com/vi/yQBImEeXNZ4/maxresdefault.jpg"))
    album3b.add_song(Song(14, "Nail Tech", 245, "https://i.ytimg.com/vi/e2AeKIzfQus/maxresdefault.jpg"))
    artist3.add_album(album3b)

    # -------------------------
    # Add artists to player
    # -------------------------
    player.add_artist(artist1)
    player.add_artist(artist2)
    player.add_artist(artist3)

    print("Initialized mock data with 3 artists (Drake, Lil Uzi Vert, Jack Harlow), albums, and songs.")
