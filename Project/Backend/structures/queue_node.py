class QueueNode:
    def __init__(self, song, index=None):
        self.song = song
        self.prev = None
        self.next = None
        self.index = index  # เก็บตำแหน่งใน queue