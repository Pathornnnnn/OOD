import React, { useState } from "react";

const QueueDisplay = ({ queue }) => {
  const [hoverIndex, setHoverIndex] = useState(null);

  // หา current index จาก queue
  const currentIndex = queue.findIndex(
    (track) => track.index === queue[0]?.index
  );

  return (
    <div className="p-4 bg-zinc-900 rounded-lg shadow-xl max-w-2xl mx-auto">
      <h2 className="text-xl font-bold text-white mb-4">🎵 Queue</h2>
      <ul className="space-y-4 relative">
        {queue.length > 0 ? (
          queue.map((track, idx) => {
            const isCurrent = idx === currentIndex;
            const isHover = idx === hoverIndex;

            return (
              <li
                key={track.index}
                className={`
                  p-3 rounded-md transition-all duration-300 relative cursor-pointer
                  ${
                    isCurrent
                      ? "bg-purple-600 text-white shadow-lg"
                      : isHover
                      ? "bg-purple-500 text-white shadow-lg"
                      : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                  }
                `}
                onMouseEnter={() => setHoverIndex(idx)}
                onMouseLeave={() => setHoverIndex(null)}
              >
                <div className="flex justify-between items-center">
                  <span
                    className={`font-medium truncate ${
                      isCurrent || isHover ? "text-white" : "text-zinc-200"
                    }`}
                  >
                    {track.title}
                  </span>
                  <span className="text-sm opacity-75">
                    {Math.floor(track.duration / 60)}:
                    {("0" + (track.duration % 60)).slice(-2)}
                  </span>
                </div>

                {idx < queue.length - 1 && (
                  <div className="absolute right-2 top-1/2 transform -translate-y-1/2 text-purple-400">
                    ➡️
                  </div>
                )}
                {idx === queue.length - 1 && queue.length > 1 && (
                  <div className="absolute right-2 top-1/2 transform -translate-y-1/2 text-purple-400 animate-pulse">
                    🔄
                  </div>
                )}
              </li>
            );
          })
        ) : (
          <li className="text-zinc-500 text-center py-4">
            The queue is empty. Add some songs!
          </li>
        )}
      </ul>
    </div>
  );
};

export default QueueDisplay;
