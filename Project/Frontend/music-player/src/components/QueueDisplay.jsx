import React from 'react';

const QueueDisplay = ({ queue, currentSongId }) => {
  return (
    <div className="p-4 bg-zinc-900 rounded-lg shadow-xl max-w-sm mx-auto">
      <h2 className="text-xl font-bold text-white mb-4">🎵 Queue</h2>
      <ul className="space-y-2">
        {queue.length > 0 ? (
          queue.map((track) => (
            <li
              key={track.id}
              // ใช้ ternary operator เพื่อตรวจสอบว่า id ของเพลงตรงกับ currentSongId หรือไม่
              className={`
                p-3 rounded-md transition-all duration-300
                ${track.id === currentSongId 
                  ? 'bg-purple-600 text-white shadow-lg hover:bg-purple-700' 
                  : 'bg-zinc-800 text-zinc-300 hover:bg-zinc-700'
                }
                cursor-pointer
              `}
            >
              <div className="flex justify-between items-center">
                <span className={`
                  font-medium truncate
                  ${track.id === currentSongId ? 'text-white' : 'text-zinc-200'}
                `}>
                  {track.title}
                </span>
                <span className="text-sm opacity-75">
                  {Math.floor(track.duration / 60)}:{('0' + (track.duration % 60)).slice(-2)}
                </span>
              </div>
            </li>
          ))
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