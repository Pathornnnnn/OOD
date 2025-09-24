import React from "react";

// --- Sub-component for a single song item ---
// Add onAddSong prop
const SongItem = ({ title, duration, onAddSong }) => {
  const formatDuration = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
  };

  return (
    // Add onClick handler
    <div
      onClick={onAddSong}
      className="flex justify-between items-center py-2 px-4 bg-gray-800 rounded-md hover:bg-purple-600 transition duration-300 ease-in-out cursor-pointer"
    >
      <span className="text-sm font-light truncate">{title}</span>
      <span className="text-xs text-gray-400 font-mono">
        {formatDuration(duration)}
      </span>
    </div>
  );
};

// --- Sub-component for a single album card ---
// Add onAddSong prop
const AlbumCard = ({ name, url, songs, onAddSong }) => {
  return (
    <div className="bg-gray-900 rounded-lg p-4 shadow-xl border border-gray-700">
      <div className="flex items-center space-x-4 mb-4">
        <img
          src={url}
          alt={name}
          className="w-16 h-16 rounded-lg object-cover border border-purple-500"
        />
        <h4 className="text-xl font-semibold text-purple-400">{name}</h4>
      </div>
      <div className="space-y-2">
        {songs.length > 0 ? (
          songs.map((song) => (
            // Pass the onAddSong function and the song's ID
            <SongItem
              key={song.id}
              title={song.title}
              duration={song.duration}
              onAddSong={() => onAddSong(song.id)}
            />
          ))
        ) : (
          <p className="text-center text-gray-500 text-sm italic">
            No songs in this album.
          </p>
        )}
      </div>
    </div>
  );
};

// --- Main Layout_Artist component ---
// Add onAddSong prop
const Layout_Artist = ({ artist, onAddSong }) => {
  if (!artist) {
    return <div>No artist data available.</div>;
  }

  const { name, url, albums } = artist;

  return (
    <div className="bg-zinc-950 p-8 rounded-3xl shadow-2xl border border-gray-800 text-white max-w-4xl mx-auto">
      {/* Artist Section */}
      <div className="flex flex-col md:flex-row items-center md:space-x-8 mb-8 pb-8 border-b border-gray-700">
        <img
          src={url}
          alt={name}
          className="w-32 h-32 rounded-full border-4 border-purple-500 shadow-xl mb-4 md:mb-0"
        />
        <div className="text-center md:text-left">
          <h1 className="text-4xl font-extrabold tracking-tight text-purple-400">
            {name}
          </h1>
          <p className="text-lg text-gray-400 mt-1">
            Explore their discography below.
          </p>
        </div>
      </div>

      {/* Albums Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {albums.length > 0 ? (
          albums.map((album) => (
            // Pass the onAddSong prop to AlbumCard
            <AlbumCard
              key={album.id}
              name={album.name}
              url={album.url}
              songs={album.songs}
              onAddSong={onAddSong}
            />
          ))
        ) : (
          <p className="text-center text-gray-500 text-lg col-span-2 italic">
            This artist has no albums.
          </p>
        )}
      </div>
    </div>
  );
};

export default Layout_Artist;
