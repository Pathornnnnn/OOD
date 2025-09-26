# Backend/core/three_level_linklist.py

from Backend.models.node import ArtistNode
from Backend.models.artist import Artist

class ThreeLevelLinkedList:
    def __init__(self):
        self.head: ArtistNode = None
        self.tail: ArtistNode = None

    def add_artist(self, artist: Artist):
        node = ArtistNode(artist)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next_artist = node
            self.tail = node

    def get_all_artists(self):
        artists = []
        current = self.head
        while current:
            artists.append(current.artist)
            current = current.next_artist
        return artists

    def get_all_songs(self):
        songs = []
        current_artist = self.head
        while current_artist:
            album_node = current_artist.head_album
            while album_node:
                songs.extend(album_node.get_songs())
                album_node = album_node.next_album
            current_artist = current_artist.next_artist
        return songs
