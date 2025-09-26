from Backend.models.song import Song
from Backend.structures.circular_doubly_linked_list import CircularDoublyLinkedList
from Backend.structures.stack_history import StackHistory

class HybridMusicPlayer:
    def __init__(self):
        self.library = Library()
        self.queue = CircularDoublyLinkedList()
        self.history = StackHistory()

    # ----------------------
    # Library Methods
    # ----------------------
    def add_artist(self, artist):
        self.library.add_artist(artist)

    def get_all_songs(self):
        return self.library.get_all_songs()

    # ----------------------
    # Queue Methods
    # ----------------------
    def add_to_queue(self, song: Song):
        if not isinstance(song, Song):
            raise ValueError("Only Song objects can be added to queue")
        self.queue.add(song)

    def remove_from_queue(self, song_id: int):
        if self.queue.head is None:
            return False
        return self.queue.remove(song_id)

    # ----------------------
    # Player Methods
    # ----------------------
    def play(self):
        song = self.queue.get_current_song()
        if song:
            self.history.push(song)
        return song

    def next(self):
        song = self.queue.next_song()
        if song:
            self.history.push(song)
        return song

    def previous(self):
        song = self.queue.previous_song()
        if song:
            self.history.push(song)
        return song

    def get_queue(self):
        return self.queue.to_list()


class Library:
    def __init__(self):
        self.artists = []

    def add_artist(self, artist):
        self.artists.append(artist)

    def get_all_songs(self):
        songs = []
        for artist in self.artists:
            for album in artist.albums:
                songs.extend(album.songs)
        return songs
