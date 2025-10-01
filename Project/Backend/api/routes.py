from fastapi import APIRouter
from Backend.core.hybrid_music_player import player
from Backend.data.mock_data import init_data
router = APIRouter()

# ------------------------------
# Init Mock Data
# ------------------------------
init_data()

# ------------------------------
# Library
# ------------------------------
@router.get("/library/songs")
def get_songs():
    # คืน dict สำหรับ UI
    return player.library.get_all_songs_dict()

@router.get("/library/artists")
def get_artists():
    # Already returns list of dicts
    return player.library.get_all_artists()

@router.get("/library/artist/{artist_id}")
def get_artist(artist_id: int):
    for artist in player.library.get_all_artists():
        if artist["id"] == artist_id:
            return artist
    return {"error": "Artist not found"}

@router.get("/library/album/{album_id}")
def get_album(album_id: int):
    current_artist = player.library.head
    while current_artist:
        album_node = current_artist.head_album
        while album_node:
            if album_node.album.id == album_id:
                return album_node.album.to_dict()
            album_node = album_node.next_album
        current_artist = current_artist.next_artist
    return {"error": "Album not found"}

# ------------------------------
# Queue
# ------------------------------
@router.get("/queue")
def get_queue():
    """Return full queue with index for UI"""
    return player.queue.to_list()

@router.post("/queue/add/{song_id}")
def add_to_queue(song_id: int):
    for song_node in player.library.get_all_songs_objects():  # SongNode objects
        if song_node.id == song_id:
            player.add_to_queue(song_node)
            return {"status": "added", "song": song_node.to_dict()}
    return {"error": "Song not found"}

@router.post("/queue/remove/{song_id}")
def remove_from_queue(song_id: int):
    removed = player.remove_from_queue(song_id)
    return {"status": "removed" if removed else "not found"}

@router.post("/queue/clear")
def clear_queue():
    player.clear_queue()
    return {"status": "cleared"}

# ------------------------------
# Player
# ------------------------------
@router.post("/player/play")
def play_song():
    song = player.play()
    return song.to_dict() if song else {"error": "No song in queue"}

@router.post("/player/next")
def next_song():
    song = player.next()
    return song.to_dict() if song else {"error": "No next song"}

@router.post("/player/previous")
def previous_song():
    song = player.previous()
    return song.to_dict() if song else {"error": "No previous song"}

@router.get("/player/current")
def current_song():
    song, idx = player.queue.get_current_song()
    if not song:
        return {"message": "No song playing"}

    # Find artist name via linked list traversal
    artist_name = "Unknown Artist"
    current_artist = player.library.head
    while current_artist:
        album_node = current_artist.head_album
        while album_node:
            for s in album_node.get_songs():
                if s.id == song.id:
                    artist_name = current_artist.name
                    break
            if artist_name != "Unknown Artist":
                break
            album_node = album_node.next_album
        if artist_name != "Unknown Artist":
            break
        current_artist = current_artist.next_artist

    return {
        "id": song.id,
        "title": song.title,
        "duration": song.duration,
        "url": song.url,
        "artist": artist_name,
        "index": idx
    }

@router.post("/player/toggle_loop")
def toggle_loop():
    """Toggle replay (loop) for queue"""
    player.queue.toggle_replay()
    return {"loop": player.queue.replay}

# ------------------------------
# History (Stack)
# ------------------------------
@router.get("/history")
def get_history():
    return player.history.to_list()

@router.post("/history/clear")
def clear_history():
    player.clear_history()
    return {"status": "cleared"}

@router.post("/history/undo")
def undo_history():
    song = player.undo_history()
    if song:
        player.queue.add(song)
    return {"status": "ok", "song": song.to_dict() if song else None}

@router.post("/history/redo")
def redo_history():
    song = player.redo_history()
    if song:
        player.queue.add(song)
    return {"status": "ok", "song": song.to_dict() if song else None}
