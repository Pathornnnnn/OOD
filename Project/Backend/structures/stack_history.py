class StackHistory:
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

    def undo(self):
        """Pop ล่าสุดออกจาก history"""
        return self.pop()

    def redo(self, song):
        """Push กลับเข้า history"""
        self.push(song)