from typing import List, Optional
from .album import Album


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
