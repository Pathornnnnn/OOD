from fastapi import APIRouter
from Backend.core.hybrid_music_player import player
from Backend.data.mock_data import init_data

router = APIRouter()

# Init Mock Data
init_data()

# ----- Library -----
@router.get("/library/songs")
def get_songs():
    return [s.to_dict() for s in player.get_all_songs()]

@router.get("/library/artists")
def get_artists():
    return [a.to_dict() for a in player.library.get_all_artists()]

@router.get("/library/artist/{artist_id}")
def get_artist(artist_id: int):
    for artist in player.library.get_all_artists():
        if artist.id == artist_id:
            return artist.to_dict()
    return {"error": "Artist not found"}

@router.get("/library/album/{album_id}")
def get_album(album_id: int):
    for artist_node in player.library.head,:
        current_artist = player.library.head
        while current_artist:
            album_node = current_artist.head_album
            while album_node:
                if album_node.album.id == album_id:
                    return album_node.album.to_dict()
                album_node = album_node.next_album
            current_artist = current_artist.next_artist
    return {"error": "Album not found"}

# ----- Queue -----
@router.get("/queue")
def get_queue():
    return player.queue.to_list()

@router.post("/queue/add/{song_id}")
def add_to_queue(song_id: int):
    for artist_node in player.library.get_all_artists():
        artist_node_obj = player.library.head
        while artist_node_obj:
            album_node = artist_node_obj.head_album
            while album_node:
                for song in album_node.get_songs():
                    if song.id == song_id:
                        player.add_to_queue(song)
                        return {"status": "added", "song": song.to_dict()}
                album_node = album_node.next_album
            artist_node_obj = artist_node_obj.next_artist
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

# ----- History -----
@router.post("/history/clear")
def clear_history():
    player.clear_history()
    return {"status": "cleared"}

@router.post("/queue/clear")
def clear_queue():
    player.clear_queue()
    return {"status": "cleared"}
