import React from "react";

const QueueItem = ({ song, onRemove, index }) => {
  return (
    <div className="flex justify-between items-center p-3 mb-2 bg-gray-800 rounded-lg hover:bg-purple-600 transition cursor-pointer">
      <div className="flex flex-col">
        <span className="text-white font-semibold">{song.title}</span>
        <span className="text-gray-400 text-sm">
          {song.artist} - {song.album}
        </span>
      </div>
      <button
        onClick={() => onRemove(song.id)}
        className="text-red-500 hover:text-red-400 font-bold"
      >
        Remove
      </button>
    </div>
  );
};

export default QueueItem;
