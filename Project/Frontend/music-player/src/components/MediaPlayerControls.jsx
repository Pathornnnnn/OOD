import React, { useState, useEffect } from "react";
import {
  FaPlay,
  FaPause,
  FaStepForward,
  FaStepBackward,
  FaRandom, // Shuffle
  FaVolumeUp,
  FaVolumeMute,
  FaRedoAlt, // Loop/Repeat
} from "react-icons/fa";

const MediaPlayerControls = ({
  currentSong, // { id, title, duration, artist, albumCoverUrl }
  isPlaying, // boolean
  currentTime, // current playback time in seconds
  totalDuration, // total duration of current song in seconds
  onPlayPause, // function to toggle play/pause
  onNext, // function to skip to next song
  onPrevious, // function to skip to previous song
  onSeek, // function (newTimeInSeconds) to seek
  onShuffle, // function to toggle shuffle mode
  onToggleMute, // function to toggle mute
  onSetVolume, // function (newVolume) to set volume
  isMuted, // boolean
  volume, // 0-100
  onToggleLoop, // function to toggle loop mode
  isLooping, // boolean
}) => {
  const [localVolume, setLocalVolume] = useState(volume); // Local state for volume slider

  useEffect(() => {
    setLocalVolume(volume); // Sync local volume with prop
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
    const newProgressPercentage = (clickPosition / rect.width) * 100;

    const newProgressTime = (newProgressPercentage / 100) * totalDuration;

    if (onSeek) {
      onSeek(newProgressTime);
    }
  };

  const handleVolumeChange = (event) => {
    const newVolume = parseInt(event.target.value, 10);
    setLocalVolume(newVolume); // Update local state immediately for smooth slider
    if (onSetVolume) {
      onSetVolume(newVolume); // Call parent handler
    }
  };

  return (
    <div className="flex flex-col items-center p-6 bg-zinc-900 rounded-xl shadow-2xl max-w-2xl mx-auto border border-gray-800">
      {/* Current Song Info */}
      <div className="flex items-center space-x-4 mb-6 w-full">
        <img
          src={
            currentSong?.url || "https://via.placeholder.com/64?text=No+Cover"
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

      {/* Main Controls (Previous, Play/Pause, Next) */}
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

      {/* Additional Controls (Shuffle, Loop, Volume) */}
      <div className="flex items-center justify-between w-full text-gray-400 text-sm mt-4">
        {/* Shuffle Button */}
        <button
          onClick={onShuffle}
          className={`p-2 rounded-full transition-colors duration-200 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-600 
            ${
              onShuffle ? "text-purple-400" : "text-gray-400"
            } // Highlight if shuffle is active (adjust logic based on your shuffle state)
          `}
        >
          <FaRandom size={16} />
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
            style={{ "--tw-accent-color": "#9333ea" }} // Custom accent color for input range
          />
        </div>

        {/* Loop Button */}
        <button
          onClick={onToggleLoop}
          className={`p-2 rounded-full transition-colors duration-200 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-600
            ${isLooping ? "text-purple-400" : "text-gray-400"}
          `}
        >
          <FaRedoAlt size={16} />
        </button>
      </div>
    </div>
  );
};

export default MediaPlayerControls;
