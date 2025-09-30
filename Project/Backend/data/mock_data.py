from Backend.models.node import ArtistNode
from Backend.core.hybrid_music_player import player
def print_library(head_artist):
    """เดิน linked list ของ library ทั้งหมดแล้ว print ออกมาเป็น tree"""
    current_artist = head_artist
    while current_artist:
        print(f"🎤 Artist {current_artist.id}: {current_artist.name} ({current_artist.url})")
        current_album = current_artist.head_album
        while current_album:
            print(f"   📀 Album {current_album.id}: {current_album.name} ({current_album.url})")
            current_song = current_album.head_song
            while current_song:
                print(f"      🎵 Song {current_song.id}: {current_song.title} "
                      f"({current_song.duration}s, {current_song.url})")
                current_song = current_song.next_song
            current_album = current_album.next_album
        current_artist = current_artist.next_artist


def init_data():
    # -------------------------
    # Artist 1: Drake
    # -------------------------
    artist1 = ArtistNode(1, "Drake", "https://upload.wikimedia.org/wikipedia/commons/2/28/Drake_July_2016.jpg")

    album1 = artist1.add_album(1, "Views", "https://upload.wikimedia.org/wikipedia/en/a/af/Drake_-_Views_cover.jpg")
    album1.add_song(1, "Hotline Bling", 210, "https://i.ytimg.com/vi/uxpDa-c-4Mc/maxresdefault.jpg")
    album1.add_song(2, "One Dance", 200, "https://i1.sndcdn.com/artworks-mS6d7vFc5d7IAkIW-L8hkzg-t500x500.jpg")

    album2 = artist1.add_album(2, "Scorpion", "https://upload.wikimedia.org/wikipedia/en/9/90/Scorpion_by_Drake.jpg")
    album2.add_song(3, "God's Plan", 220, "https://i.ytimg.com/vi/RfO1DTGwIAA/sddefault.jpg")
    album2.add_song(4, "In My Feelings", 205, "https://i.ytimg.com/vi/suz7pWi1mOs/sddefault.jpg")

    # -------------------------
    # Artist 2: Lil Uzi Vert
    # -------------------------
    artist2 = ArtistNode(2, "Lil Uzi Vert", "https://upload.wikimedia.org/wikipedia/commons/4/44/Lil_Uzi_Vert_%282018%29.png")

    album3 = artist2.add_album(3, "Luv Is Rage 2", "https://i.scdn.co/image/ab67616d0000b273f23aee9d3be9fcbca1bc6352")
    album3.add_song(5, "XO Tour Llif3", 240, "https://i.ytimg.com/vi/WrsFXgQk5UI/hqdefault.jpg")
    album3.add_song(6, "The Way Life Goes", 230, "https://i.ytimg.com/vi/Vi2XaiKhgiU/maxresdefault.jpg")

    album4 = artist2.add_album(4, "Eternal Atake", "https://i.scdn.co/image/ab67616d0000b273158b08c02c249bc651b3b47a")
    album4.add_song(7, "Baby Pluto", 215, "https://i1.sndcdn.com/artworks-z9V7CpywBmXYV8Jf-BJ5PUA-t500x500.jpg")
    album4.add_song(8, "Futsal Shuffle 2020", 225, "https://i1.sndcdn.com/artworks-1FIrnlRk17n5-0-t500x500.jpg")

    # -------------------------
    # Artist 3: Jack Harlow
    # -------------------------
    artist3 = ArtistNode(3, "Jack Harlow", "https://yt3.googleusercontent.com/6KQV9B-m_cFu0b1aUnUFfbA3IQL5xY5yYgTWwuIEPJgY8p8HzgwtotTeksTzFQtdrJBrwd7i4A=s900-c-k-c0x00ffffff-no-rj")

    album5 = artist3.add_album(5, "Thats What They All Say", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ805A5w_Nhnb4aI42h-bkiCOv8n8x1Nwx3Zg&s")
    album5.add_song(9, "Whats Poppin", 260, "https://i.ytimg.com/vi/w9uWPBDHEKE/hqdefault.jpg")
    album5.add_song(10, "Tyler Herro", 275, "https://upload.wikimedia.org/wikipedia/en/4/45/Jack_Harlow_-_Tyler_Herro.png")

    album6 = artist3.add_album(6, "Come Home the Kids Miss You", "https://i.scdn.co/image/ab67616d0000b2738e55edb69ca44a25b52b17bb")
    album6.add_song(11, "First Class", 250, "https://i.ytimg.com/vi/yQBImEeXNZ4/maxresdefault.jpg")
    album6.add_song(12, "Nail Tech", 245, "https://i.ytimg.com/vi/e2AeKIzfQus/maxresdefault.jpg")

    # -------------------------
    # Add ArtistNodes เข้า player
    # -------------------------
    player.add_artist(artist1)
    player.add_artist(artist2)
    player.add_artist(artist3)

    print("✅ Initialized mock data with pure linked list (ArtistNode -> AlbumNode -> SongNode)")
