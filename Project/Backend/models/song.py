from typing import Optional

class Song:
    _id_counter = 1  # 🔹 ตัวนับ shared ระดับ class

    def __init__(self, title: str, duration: int, url: Optional[str] = None):
        self.id = Song._id_counter  # ใช้ค่า counter ปัจจุบัน
        Song._id_counter += 1       # เพิ่ม counter
        self.title = title
        self.duration = duration
        self.url = url

    def add_url(self, url: str):
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration,
            "url": self.url,
        }
