from Backend.models.artist import Artist


class ThreeDLinkedList:
    """
    3D Linked List:
    Artist -> Album -> Song
    """
    def __init__(self):
        self.artists = []

    def add_artist(self, artist: Artist):
        self.artists.append(artist)

    def get_all_songs(self):
        songs = []
        for artist in self.artists:
            for album in artist.albums:
                songs.extend(album.songs)
        return songs

    def to_dict(self):
        return [artist.to_dict() for artist in self.artists]
