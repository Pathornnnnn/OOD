from typing import List

class Song:
    def __init__(self, id: int, title: str, duration: int):
        self.id = id
        self.title = title
        self.duration = duration

    def to_dict(self):
        return {"id": self.id, "title": self.title, "duration": self.duration}


class Album:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.songs: List[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "songs": [s.to_dict() for s in self.songs]}


class Artist:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        self.albums.append(album)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "albums": [a.to_dict() for a in self.albums]}
