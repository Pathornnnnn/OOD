from .queue_node import QueueNode

class CircularDequeQueue:
    def __init__(self, replay=False):
        self.head: QueueNode = None
        self.current: QueueNode = None
        self.replay = replay
        self.size = 0

    # Add song
    def add(self, song):
        new_node = QueueNode(song)
        new_node.index = self.size
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    # Remove first (dequeue)
    def dequeue(self):
        if not self.head:
            return None
        removed = self.head
        if self.size == 1:
            self.head = None
            self.current = None
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            if self.current == self.head:
                self.current = self.head.next
            self.head = self.head.next
            self._update_indices()
        self.size -= 1
        return removed.song

    def _update_indices(self):
        if not self.head:
            return
        curr = self.head
        idx = 0
        while True:
            curr.index = idx
            idx += 1
            curr = curr.next
            if curr == self.head:
                break

    # Remove song by id
    def remove(self, song_id):
        if not self.head:
            return False
        curr = self.head
        while True:
            if curr.song.id == song_id:
                if self.size == 1:
                    self.head = None
                    self.current = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                    if curr == self.current:
                        self.current = curr.next
                    self._update_indices()
                self.size -= 1
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    # Playback
    def next_song(self):
        if not self.current:
            return None
        song = self.current.song
        if self.replay:
            self.current = self.current.next
        else:
            self.dequeue()
        return song

    def previous_song(self):
        if not self.current:
            return None
        self.current = self.current.prev
        return self.current.song

    def get_current_song(self):
        return self.current.song if self.current else None

    def clear(self):
        self.head = None
        self.current = None
        self.size = 0

    def to_list(self):
        songs = []
        if not self.head:
            return songs
        curr = self.head
        while True:
            songs.append({
                **curr.song.to_dict(),
                "index": curr.index
            })
            curr = curr.next
            if curr == self.head:
                break
        return songs

    # Toggle replay
    def toggle_replay(self):
        self.replay = not self.replay
        return self.replay
