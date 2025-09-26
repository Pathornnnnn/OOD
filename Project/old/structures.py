# Circular Doubly Linked List สำหรับ Play Queue
class QueueNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def add(self, song):
        new_node = QueueNode(song)
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

    def remove(self, song_id):
        if not self.head:
            return False

        curr = self.head
        while True:
            if curr.song.id == song_id:
                if curr == self.head and curr.next == self.head:
                    self.head = None
                    self.current = None
                    return True
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                    if curr == self.current:
                        self.current = curr.next
                    return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def next_song(self):
        if self.current:
            self.current = self.current.next
            return self.current.song
        return None

    def previous_song(self):
        if self.current:
            self.current = self.current.prev
            return self.current.song
        return None

    def get_current_song(self):
        return self.current.song if self.current else None

    def to_list(self):
        songs = []
        if not self.head:
            return songs
        curr = self.head
        while True:
            songs.append(curr.song.to_dict())
            curr = curr.next
            if curr == self.head:
                break
        return songs


# Stack สำหรับ History
class Stack:
    def __init__(self):
        self.items = []

    def push(self, song):
        self.items.append(song)

    def pop(self):
        return self.items.pop() if self.items else None

    def to_list(self):
        return [song.to_dict() for song in reversed(self.items)]

    def clear(self):
        self.items = []
