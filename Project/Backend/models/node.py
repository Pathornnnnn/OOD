from typing import Optional
from Backend.models.artist import Artist
from Backend.models.album import Album
from Backend.models.song import Song

class SongNode:
    def __init__(self, song: Song):
        self.song = song
        self.next_song: Optional["SongNode"] = None

class AlbumNode:
    def __init__(self, album: Album):
        self.album = album
        self.next_album: Optional["AlbumNode"] = None
        self.head_song: Optional[SongNode] = None
        self.tail_song: Optional[SongNode] = None
        for s in album.songs:
            self.add_song(s)

    def add_song(self, song: Song):
        node = SongNode(song)
        if not self.head_song:
            self.head_song = self.tail_song = node
        else:
            self.tail_song.next_song = node
            self.tail_song = node

    def get_songs(self):
        songs = []
        current = self.head_song
        while current:
            songs.append(current.song)
            current = current.next_song
        return songs

class ArtistNode:
    def __init__(self, artist: Artist):
        self.artist = artist
        self.next_artist: Optional["ArtistNode"] = None
        self.head_album: Optional[AlbumNode] = None
        self.tail_album: Optional[AlbumNode] = None
        for al in artist.albums:
            self.add_album(al)

    def add_album(self, album: Album):
        node = AlbumNode(album)
        if not self.head_album:
            self.head_album = self.tail_album = node
        else:
            self.tail_album.next_album = node
            self.tail_album = node

    def get_albums(self):
        albums = []
        current = self.head_album
        while current:
            albums.append(current.album)
            current = current.next_album
        return albums
