from library import MusicLibrary3D
from queue import CircularDoublyLinkedList
from stack import Stack
from entities import Artist, Song


class HybridMusicPlayer:
    def __init__(self):
        self.library = MusicLibrary3D()
        self.queue = CircularDoublyLinkedList()
        self.history = Stack()

    def add_artist(self, artist: Artist):
        return self.library.add_artist(artist)

    def add_to_queue(self, song: Song):
        self.queue.add(song)

    def remove_from_queue(self, song_id: int):
        return self.queue.remove(song_id)

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

    def get_all_songs(self):
        return [s.to_dict() for s in self.library.get_all_songs()]
