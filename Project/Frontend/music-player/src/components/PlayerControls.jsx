import { useState, useRef, useEffect } from "react";
import {
  Play,
  Pause,
  SkipForward,
  SkipBack,
  Volume2,
  Shuffle,
  Repeat,
  Square,
} from "lucide-react";

export default function MusicPlayer({ playlist = [], startIndex = 0 }) {
  const [currentIndex, setCurrentIndex] = useState(startIndex);
  const [isPlaying, setIsPlaying] = useState(false);
  const [shuffle, setShuffle] = useState(false);
  const [repeat, setRepeat] = useState(false);
  const [progress, setProgress] = useState(0);
  const audioRef = useRef(null);

  const currentSong = playlist[currentIndex];

  // อัพเดท progress bar ตามเวลาเล่นจริง
  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const updateProgress = () => {
      setProgress((audio.currentTime / audio.duration) * 100 || 0);
    };

    audio.addEventListener("timeupdate", updateProgress);
    audio.addEventListener("ended", handleNext);

    return () => {
      audio.removeEventListener("timeupdate", updateProgress);
      audio.removeEventListener("ended", handleNext);
    };
  }, [currentIndex, repeat, shuffle]);

  // Play / Pause
  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play();
    }
    setIsPlaying(!isPlaying);
  };

  // Stop
  const handleStop = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    audioRef.current.currentTime = 0;
    setIsPlaying(false);
    setProgress(0);
  };

  // Next
  const handleNext = () => {
    if (repeat) {
      audioRef.current.currentTime = 0;
      audioRef.current.play();
      return;
    }

    let nextIndex;
    if (shuffle) {
      nextIndex = Math.floor(Math.random() * playlist.length);
    } else {
      nextIndex = (currentIndex + 1) % playlist.length;
    }
    setCurrentIndex(nextIndex);
    setIsPlaying(true);
  };

  // Previous
  const handlePrevious = () => {
    let prevIndex;
    if (shuffle) {
      prevIndex = Math.floor(Math.random() * playlist.length);
    } else {
      prevIndex = (currentIndex - 1 + playlist.length) % playlist.length;
    }
    setCurrentIndex(prevIndex);
    setIsPlaying(true);
  };

  // Seek
  const handleSeek = (e) => {
    if (!audioRef.current) return;
    const value = e.target.value;
    audioRef.current.currentTime = (value / 100) * audioRef.current.duration;
    setProgress(value);
  };

  // Volume
  const handleVolume = (e) => {
    if (!audioRef.current) return;
    audioRef.current.volume = e.target.value;
  };

  return (
    <div className="flex flex-col items-center gap-4 bg-gray-900 text-white p-6 rounded-xl w-full max-w-md">
      {/* Audio */}
      {currentSong && (
        <audio
          ref={audioRef}
          src={`/assets/music/${currentSong.id}.mp3`}
          autoPlay={isPlaying}
        />
      )}

      {/* Title */}
      <h2 className="text-lg font-semibold">
        {currentSong ? currentSong.title : "No Song"}
      </h2>

      {/* Progress Bar */}
      <div className="flex items-center gap-2 w-full">
        <input
          type="range"
          min="0"
          max="100"
          step="0.1"
          value={progress}
          onChange={handleSeek}
          className="w-full accent-green-500"
        />
      </div>

      {/* Controls */}
      <div className="flex items-center gap-6 mt-2">
        <Shuffle
          className={`cursor-pointer ${shuffle ? "text-green-500" : ""}`}
          onClick={() => setShuffle(!shuffle)}
        />
        <SkipBack className="cursor-pointer" onClick={handlePrevious} />

        <button
          onClick={togglePlay}
          className="w-14 h-14 flex items-center justify-center rounded-full bg-white text-black"
        >
          {isPlaying ? <Pause size={28} /> : <Play size={28} />}
        </button>

        <SkipForward className="cursor-pointer" onClick={handleNext} />
        <Repeat
          className={`cursor-pointer ${repeat ? "text-green-500" : ""}`}
          onClick={() => setRepeat(!repeat)}
        />
        <Square className="cursor-pointer" onClick={handleStop} />
      </div>

      {/* Volume */}
      <div className="flex items-center gap-2 mt-4">
        <Volume2 />
        <input
          type="range"
          min="0"
          max="1"
          step="0.01"
          defaultValue="1"
          onChange={handleVolume}
          className="w-32 accent-green-500"
        />
      </div>
    </div>
  );
}
