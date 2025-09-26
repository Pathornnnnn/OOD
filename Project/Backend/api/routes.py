from fastapi import APIRouter
from Backend.core.hybrid_music_player import HybridMusicPlayer
from Backend.models.artist import Artist
from Backend.models.album import Album
from Backend.models.song import Song
from Backend.data.mock_data import init_data, player

router = APIRouter()

# Init Mock Data
init_data()

# ----- Library -----
@router.get("/library/songs")
def get_songs():
    return [s.to_dict() for s in player.get_all_songs()]

@router.get("/library/artists")
def get_artists():
    return [a.to_dict() for a in player.library.artists]

@router.get("/library/artist/{artist_id}")
def get_artist(artist_id: int):
    for a in player.library.artists:
        if a.id == artist_id:
            return a.to_dict()
    return {"error": "Artist not found"}

@router.get("/library/album/{album_id}")
def get_album(album_id: int):
    for a in player.library.artists:
        for al in a.albums:
            if al.id == album_id:
                return al.to_dict()
    return {"error": "Album not found"}

# ----- Queue -----
@router.get("/queue")
def get_queue():
    return player.queue.to_list()

@router.post("/queue/add/{song_id}")
def add_to_queue(song_id: int):
    for a in player.library.artists:
        for al in a.albums:
            for s in al.songs:
                if s.id == song_id:
                    player.add_to_queue(s)
                    return {"status": "added", "song": s.to_dict()}
    return {"error": "Song not found"}

@router.post("/queue/remove/{song_id}")
def remove_from_queue(song_id: int):
    removed = player.remove_from_queue(song_id)
    return {"status": "removed" if removed else "not found"}

# ----- Player -----
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
    song = player.queue.get_current_song()
    return song.to_dict() if song else {"error": "No song playing"}

# ----- History -----
@router.get("/history")
def get_history():
    return player.history.to_list()

@router.post("/history/clear")
def clear_history():
    player.history.clear()
    return {"status": "cleared"}
