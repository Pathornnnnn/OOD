# stack_history.py
class StackHistory:
    def __init__(self):
        self.items = []
        self.redo_stack = []

    def push(self, song, song_id):
        """Push ใหม่ แล้วล้าง redo stack"""
        self.items.append({"song": song, "id": song_id})
        self.redo_stack.clear()

    def push_direct(self, song, song_id):
        """ใช้สำหรับ redo ไม่ล้าง redo stack"""
        self.items.append({"song": song, "id": song_id})

    def pop(self):
        if not self.items:
            return None
        item = self.items.pop()
        self.redo_stack.append(item)
        return item["song"]

    def undo(self):
        return self.pop()

    def redo(self):
        if not self.redo_stack:
            return None
        item = self.redo_stack.pop()
        self.push_direct(item["song"], item["id"])
        return item["song"]

    def to_list(self):
        return [item["song"].to_dict() for item in self.items]

    def clear(self):
        self.items = []
        self.redo_stack = []
