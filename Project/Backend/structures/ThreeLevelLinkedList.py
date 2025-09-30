from Backend.models.node import *
class ThreeLevelLinkedList:
    def __init__(self):
        self.head: ArtistNode = None
        self.tail: ArtistNode = None

    def add_artist(self, artist_node: ArtistNode):
        if not self.head:
            self.head = self.tail = artist_node
        else:
            self.tail.next_artist = artist_node
            self.tail = artist_node

    def get_all_artists(self):
        artists = []
        current = self.head
        while current:
            artists.append(current.to_dict())
            current = current.next_artist
        return artists



    def get_all_songs_objects(self):
        songs = []
        current_artist = self.head
        while current_artist:
            album_node = current_artist.head_album
            while album_node:
                songs.extend(album_node.get_songs())  # Song objects
                album_node = album_node.next_album
            current_artist = current_artist.next_artist
        return songs

    def get_all_songs_dict(self):
        songs = []
        current_artist = self.head
        while current_artist:
            album_node = current_artist.head_album
            while album_node:
                songs.extend([s.to_dict() for s in album_node.get_songs()])  # dict สำหรับ API
                album_node = album_node.next_album
            current_artist = current_artist.next_artist
        return songs