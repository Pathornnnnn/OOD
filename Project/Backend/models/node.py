from typing import Optional

# -------------------------
# Song Node
# -------------------------
class SongNode:
    def __init__(self, id: int, title: str, duration: int, url: Optional[str] = None):
        self.id = id
        self.title = title
        self.duration = duration
        self.url = url
        self.next_song: Optional["SongNode"] = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration,
            "url": self.url,
        }


# -------------------------
# Album Node
# -------------------------
class AlbumNode:
    def __init__(self, id: int, name: str, url: Optional[str] = None):
        self.id = id
        self.name = name
        self.url = url
        self.head_song: Optional[SongNode] = None
        self.tail_song: Optional[SongNode] = None
        self.next_album: Optional["AlbumNode"] = None

    def add_song(self, id: int, title: str, duration: int, url: Optional[str] = None):
        node = SongNode(id, title, duration, url)
        if not self.head_song:
            self.head_song = self.tail_song = node
        else:
            self.tail_song.next_song = node
            self.tail_song = node

    def get_songs(self):
        songs = []
        current = self.head_song
        while current:
            songs.append(current)
            current = current.next_song
        return songs

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "songs": [song.to_dict() for song in self.get_songs()]
        }

# -------------------------
# Artist Node
# -------------------------
class ArtistNode:
    def __init__(self, id: int, name: str, url: Optional[str] = None):
        self.id = id
        self.name = name
        self.url = url
        self.head_album: Optional[AlbumNode] = None
        self.tail_album: Optional[AlbumNode] = None
        self.next_artist: Optional["ArtistNode"] = None

    def add_album(self, id: int, name: str, url: Optional[str] = None) -> AlbumNode:
        node = AlbumNode(id, name, url)
        if not self.head_album:
            self.head_album = self.tail_album = node
        else:
            self.tail_album.next_album = node
            self.tail_album = node
        return node

    def get_albums(self):
        albums = []
        current = self.head_album
        while current:
            albums.append(current)
            current = current.next_album
        return albums

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "albums": [album.to_dict() for album in self.get_albums()]
        }

# queue_node.py
class QueueNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
        self.index = -1
