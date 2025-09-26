from typing import List, Optional

class Song:
    def __init__(self, id: int, title: str, duration: int, url: Optional[str] = None):
        self.id = id
        self.title = title
        self.duration = duration
        self.url = url

    def add_url(self, url: str):
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration,
            "url": self.url,
        }


class Album:
    def __init__(self, id: int, name: str, url: Optional[str] = None):
        self.id = id
        self.name = name
        self.url = url
        self.songs: List[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def add_url(self, url: str):
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "songs": [s.to_dict() for s in self.songs],
        }


class Artist:
    def __init__(self, id: int, name: str, url: Optional[str] = None):
        self.id = id
        self.name = name
        self.url = url
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        self.albums.append(album)

    def add_url(self, url: str):
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "albums": [a.to_dict() for a in self.albums],
        }
