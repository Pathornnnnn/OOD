import React from "react";
import SongItem from "./SongItem.jsx";

const AlbumCard = ({ album, onAddSong }) => {
  const { name, url, songs } = album;

  return (
    <div className="bg-gray-900 rounded-lg p-4 shadow-xl border border-gray-700">
      <div className="flex items-center space-x-4 mb-4">
        <img src={url} alt={name} className="w-16 h-16 rounded-lg object-cover border border-purple-500"/>
        <h4 className="text-xl font-semibold text-purple-400">{name}</h4>
      </div>
      <div className="space-y-2">
        {songs.length > 0 ? (
          songs.map((song) => (
            <SongItem
              key={song.id}
              song={song}
              onAddSong={() => onAddSong(song.id)}
            />
          ))
        ) : (
          <p className="text-center text-gray-500 italic text-sm">No songs</p>
        )}
      </div>
    </div>
  );
};

export default AlbumCard;
