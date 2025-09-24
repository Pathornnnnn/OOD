from Backend.structures import CircularDoublyLinkedList, Stack

class HybridMusicPlayer:
    def __init__(self):
        self.library = []
        self.queue = CircularDoublyLinkedList()
        self.history = Stack()

    def add_artist(self, artist):
        self.library.append(artist)

    def add_to_queue(self, song):
        self.queue.add(song)

    def remove_from_queue(self, song_id):
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
        songs = []
        for artist in self.library:
            for album in artist.albums:
                songs.extend(album.songs)
        return songs
