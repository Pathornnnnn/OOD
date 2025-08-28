export default function SongList({ songs, onSelect }) {
  return (
    <div className="space-y-2 bg-gray-900 p-4 rounded-lg text-white shadow-lg">
      <h3 className="text-xl font-bold mb-3 border-b border-yellow-500 pb-1">
        Rap / Hip-Hop Tracks
      </h3>
      {songs.map((song) => (
        <div
          key={song.id}
          className="flex justify-between items-center p-2 hover:bg-gray-700 rounded-lg cursor-pointer transition-colors duration-200"
          onClick={() => onSelect(song)}
        >
          <div className="font-semibold">{song.title}</div>
          <div className="text-sm text-gray-300">
            {song.duration
              ? `${Math.floor(song.duration / 60)}:${String(
                  song.duration % 60
                ).padStart(2, "0")}`
              : ""}
          </div>
        </div>
      ))}
    </div>
  );
}

