import React from "react";

const SongItem = ({ song, onAddSong }) => {
  const formatDuration = (sec) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m}:${s < 10 ? "0" : ""}${s}`;
  };

  return (
    <div
      onClick={onAddSong}
      className="flex justify-between items-center py-2 px-4 bg-gray-800 rounded-md hover:bg-purple-600 transition duration-300 cursor-pointer"
    >
      <span className="text-sm font-light truncate">{song.title}</span>
      <span className="text-xs text-gray-400 font-mono">{formatDuration(song.duration)}</span>
    </div>
  );
};

export default SongItem;
