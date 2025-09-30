# circular_deque_queue.py
from Backend.models.node import QueueNode

class CircularDequeQueue:
    def __init__(self, replay=False):
        self.head: QueueNode = None
        self.current: QueueNode = None
        self.replay = replay
        self.size = 0
        self.last_pushed_id = None  # ป้องกัน duplicate push

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

    def next_song(self, history_stack=None, force_dequeue=True):
        if not self.current:
            return None

        song = self.current.song

        if self.replay:
            self.current = self.current.next
        else:
            if force_dequeue:
                removed_song = song

                if self.size == 1:
                    # 🔹 เพลงเดียว: dequeue และ queue ว่าง
                    self.head = None
                    self.current = None
                    self.size = 0
                else:
                    prev_node = self.current.prev
                    next_node = self.current.next

                    # fix links
                    prev_node.next = next_node
                    next_node.prev = prev_node

                    # update head if needed
                    if self.current == self.head:
                        self.head = next_node

                    # move current pointer
                    self.current = next_node

                    # update indices
                    self._update_indices()

                    self.size -= 1

                # push to history
                if history_stack and (self.last_pushed_id != removed_song.id):
                    history_stack.push(removed_song, removed_song.id)
                    self.last_pushed_id = removed_song.id
            else:
                self.current = self.current.next

        return song

    def previous_song(self, history_stack=None, force_dequeue=True):
        if not self.current:
            return None

        song = self.current.song

        if self.replay:
            self.current = self.current.prev
        else:
            if force_dequeue:
                removed_song = song

                if self.size == 1:
                    # 🔹 เพลงเดียว: dequeue และ queue ว่าง
                    self.head = None
                    self.current = None
                    self.size = 0
                else:
                    prev_node = self.current.prev
                    next_node = self.current.next

                    # fix links
                    prev_node.next = next_node
                    next_node.prev = prev_node

                    # update head if needed
                    if self.current == self.head:
                        self.head = next_node

                    # move current pointer backward
                    self.current = prev_node

                    # update indices
                    self._update_indices()

                    self.size -= 1

                # push to history
                if history_stack and (self.last_pushed_id != removed_song.id):
                    history_stack.push(removed_song, removed_song.id)
                    self.last_pushed_id = removed_song.id
            else:
                self.current = self.current.prev

        return song

    def get_current_song(self):
        if not self.current:
            return None, -1
        return self.current.song, self.current.index

    def clear(self):
        self.head = None
        self.current = None
        self.size = 0
        self.last_pushed_id = None

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

    def toggle_replay(self):
        self.replay = not self.replay
        return self.replay
