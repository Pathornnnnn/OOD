import React, { useState, useEffect } from "react";
import {
  FaPlay,
  FaPause,
  FaStepForward,
  FaStepBackward,
  FaVolumeUp,
  FaVolumeMute,
  FaRedoAlt,
} from "react-icons/fa";

const MediaPlayerControls = ({
  currentSong,
  isPlaying,
  currentTime,
  totalDuration,
  onPlayPause,
  onNext,
  onPrevious,
  onSeek,
  onToggleMute,
  onSetVolume,
  isMuted,
  volume,
  onToggleLoop,
  isLooping,
}) => {
  const [localVolume, setLocalVolume] = useState(volume);
  const [hoverLoop, setHoverLoop] = useState(false); // hover state

  useEffect(() => {
    setLocalVolume(volume);
  }, [volume]);

  const formatTime = (seconds) => {
    if (isNaN(seconds) || seconds < 0) return "0:00";
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
  };

  const progressPercentage =
    totalDuration > 0 ? (currentTime / totalDuration) * 100 : 0;

  const handleProgressBarClick = (event) => {
    const progressBar = event.target.closest(".progress-bar-container");
    if (!progressBar) return;
    const rect = progressBar.getBoundingClientRect();
    const clickPosition = event.clientX - rect.left;
    const newProgressTime = (clickPosition / rect.width) * totalDuration;
    if (onSeek) onSeek(newProgressTime);
  };

  const handleVolumeChange = (event) => {
    const newVolume = parseInt(event.target.value, 10);
    setLocalVolume(newVolume);
    if (onSetVolume) onSetVolume(newVolume);
  };

  return (
    <div className="flex flex-col items-center p-6 bg-zinc-900 rounded-xl shadow-2xl max-w-2xl mx-auto border border-gray-800">
      {/* Current Song Info */}
      <div className="flex items-center space-x-4 mb-6 w-full">
        <img
          src={
            currentSong?.url ||
            "https://t4.ftcdn.net/jpg/05/39/89/77/360_F_539897708_p3V5664JtSgb2CMRDV7QnqUJ9eqhLLqy.jpg"
          }
          alt={currentSong?.title || "No song playing"}
          className="w-16 h-16 rounded-lg object-cover shadow-md"
        />
        <div className="flex-1">
          <h3 className="text-xl font-bold text-white truncate">
            {currentSong?.title || "Not Playing"}
          </h3>
          <p className="text-sm text-gray-400">
            {currentSong?.artist || "Unknown Artist"}
          </p>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full mb-6">
        <div
          className="progress-bar-container w-full h-2 bg-zinc-700 rounded-full cursor-pointer group"
          onClick={handleProgressBarClick}
        >
          <div
            className="h-2 bg-purple-600 rounded-full transition-all duration-100 ease-linear group-hover:bg-purple-500"
            style={{ width: `${progressPercentage}%` }}
          ></div>
        </div>
        <div className="flex justify-between w-full text-zinc-400 text-xs mt-2 font-mono">
          <span>{formatTime(currentTime)}</span>
          <span>{formatTime(totalDuration)}</span>
        </div>
      </div>

      {/* Main Controls */}
      <div className="flex items-center justify-center space-x-6 mb-6">
        <button
          onClick={onPrevious}
          className="p-3 text-white rounded-full transition-colors duration-200 ease-in-out hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
        >
          <FaStepBackward size={20} />
        </button>

        <button
          onClick={onPlayPause}
          className="p-5 text-white bg-purple-600 rounded-full transition-colors duration-200 ease-in-out hover:bg-purple-700 focus:outline-none focus:ring-4 focus:ring-purple-800 shadow-xl"
        >
          {isPlaying ? <FaPause size={28} /> : <FaPlay size={28} />}
        </button>

        <button
          onClick={onNext}
          className="p-3 text-white rounded-full transition-colors duration-200 ease-in-out hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
        >
          <FaStepForward size={20} />
        </button>
      </div>

      {/* Loop/Replay and Volume */}
      <div className="flex items-center justify-between w-full text-gray-400 text-sm mt-4">
        {/* Replay/Loop Button */}
        {/* Replay/Loop Button */}
        <button
          onClick={() => {
            console.log("Loop button clicked! Previous isLooping:", isLooping);
            onToggleLoop?.();
          }}
          onMouseEnter={() => {
            console.log("Loop hover enter");
            setHoverLoop(true);
          }}
          onMouseLeave={() => {
            console.log("Loop hover leave");
            setHoverLoop(false);
          }}
          className={`p-2 rounded-full transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-gray-600 ${
            isLooping || hoverLoop
              ? "text-purple-400 hover:text-purple-500 bg-gray-800"
              : "text-gray-400 hover:bg-gray-700"
          }`}
        >
          <FaRedoAlt size={16} />
        </button>

        {/* Volume Control */}
        <div className="flex items-center space-x-2 flex-grow mx-4">
          <button
            onClick={onToggleMute}
            className="text-gray-400 hover:text-white transition-colors"
          >
            {isMuted || localVolume === 0 ? (
              <FaVolumeMute size={16} />
            ) : (
              <FaVolumeUp size={16} />
            )}
          </button>
          <input
            type="range"
            min="0"
            max="100"
            value={localVolume}
            onChange={handleVolumeChange}
            className="w-full h-1 bg-zinc-700 rounded-lg appearance-none cursor-pointer range-sm accent-purple-600"
          />
        </div>
      </div>
    </div>
  );
};

export default MediaPlayerControls;
