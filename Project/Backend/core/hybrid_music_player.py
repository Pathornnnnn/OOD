from Backend.models.song import Song
from Backend.structures.ThreeLevelLinkedList import ThreeLevelLinkedList
from Backend.structures.CircularDequeQueue import CircularDequeQueue
from Backend.structures.stack_history import StackHistory
from Backend.models.node import ArtistNode, SongNode


class HybridMusicPlayer:
    def __init__(self):
        # ใช้ ThreeLevelLinkedList (node-based) สำหรับ library
        self.library = ThreeLevelLinkedList()
        # Queue เป็น circular doubly linked list
        self.queue = CircularDequeQueue()
        # History เป็น stack
        self.history = StackHistory()

    # ----------------------
    # Library Methods
    # ----------------------
    def add_artist(self, artist_node: ArtistNode):
        """เพิ่ม artist (node) เข้า library"""
        self.library.add_artist(artist_node)

    def get_all_songs(self):
        """คืน list ของ Song ทั้งหมดใน library"""
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

    def clear_queue(self):
        """ล้าง queue ทั้งหมด"""
        self.queue.clear()

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

    # ----------------------
    # History Methods
    # ----------------------
    def clear_history(self):
        """ล้างประวัติเพลง"""
        self.history.clear()


# ----------------------
# Global Player Instance
# ----------------------
player = HybridMusicPlayer()
