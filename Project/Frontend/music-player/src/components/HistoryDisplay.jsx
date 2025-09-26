import React from "react";

const HistoryDisplay = ({ history, currentSongId }) => {
  return (
    <div className="p-4 bg-zinc-900 rounded-lg shadow-xl max-w-md mx-auto">
      <h2 className="text-xl font-bold text-white mb-4">🗂️ History (Stack)</h2>
      <ul className="space-y-4">
        {history.length > 0 ? (
          [...history].reverse().map((track, idx) => (
            <li
              key={track.id}
              className={`
                p-3 rounded-md transition-all duration-300
                ${
                  track.id === currentSongId
                    ? "bg-purple-600 text-white shadow-lg hover:bg-purple-700"
                    : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                }
                relative cursor-pointer
              `}
            >
              <div className="flex justify-between items-center">
                <span
                  className={`font-medium truncate ${
                    track.id === currentSongId ? "text-white" : "text-zinc-200"
                  }`}
                >
                  {track.title}
                </span>
                <span className="text-sm opacity-75">
                  {Math.floor(track.duration / 60)}:
                  {("0" + (track.duration % 60)).slice(-2)}
                </span>
              </div>
              {/* Arrow แสดง Stack push */}
              {idx < history.length - 1 && (
                <div className="absolute right-2 top-1/2 transform -translate-y-1/2 text-green-400 animate-bounce">
                  ⬆️
                </div>
              )}
            </li>
          ))
        ) : (
          <li className="text-zinc-500 text-center py-4">
            History is empty. Play some songs!
          </li>
        )}
      </ul>
    </div>
  );
};

export default HistoryDisplay;
