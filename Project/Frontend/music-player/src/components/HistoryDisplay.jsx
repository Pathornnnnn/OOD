import React from "react";

const HistoryDisplay = ({ history, currentSongId, onUndo, onRedo }) => {
  return (
    <div className="p-4 bg-zinc-900 rounded-lg shadow-xl max-w-xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-white">🗂️ History (Stack)</h2>
        <div className="flex gap-2">
          <button
            onClick={onUndo}
            className="bg-red-600 text-white px-3 py-1 rounded-md hover:bg-red-700 transition"
          >
            Undo
          </button>
          <button
            onClick={onRedo}
            className="bg-green-600 text-white px-3 py-1 rounded-md hover:bg-green-700 transition"
          >
            Redo
          </button>
        </div>
      </div>

      <ul className="space-y-4 px-4">
        {history.length > 0 ? (
          [...history].reverse().map((track) => (
            <li
              key={track.id}
              className={`p-3 rounded-md transition-all duration-300 relative cursor-pointer gap-5
              `}
            >
              <div className="flex justify-between items-center gap-5">
                <span className="font-medium truncate">{track.title}</span>
                <span className="text-sm opacity-75">
                  {Math.floor(track.duration / 60)}:
                  {("0" + (track.duration % 60)).slice(-2)}
                </span>
              </div>
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
