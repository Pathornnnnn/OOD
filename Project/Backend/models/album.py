from typing import List, Optional
from .song import Song


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
