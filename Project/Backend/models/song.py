from typing import Optional


class Song:
    def __init__(self, id: int, title: str, duration: int, url: Optional[str] = None):
        self.id = id
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
