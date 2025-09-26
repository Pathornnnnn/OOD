class QueueNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
