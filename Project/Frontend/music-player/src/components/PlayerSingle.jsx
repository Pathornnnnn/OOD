import { useState, useRef, useEffect } from "react";
import { Play, Pause, Square, Volume2 } from "lucide-react";

export default function MusicPlayerSingle() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const audioRef = useRef(null);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const updateProgress = () => {
      setProgress((audio.currentTime / audio.duration) * 100 || 0);
    };

    audio.addEventListener("timeupdate", updateProgress);
    return () => {
      audio.removeEventListener("timeupdate", updateProgress);
    };
  }, []);

  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play();
    }
    setIsPlaying(!isPlaying);
  };

  const handleStop = () => {
    if (!audioRef.current) return;
    audioRef.current.pause();
    audioRef.current.currentTime = 0;
    setIsPlaying(false);
    setProgress(0);
  };

  const handleSeek = (e) => {
    if (!audioRef.current) return;
    const value = e.target.value;
    audioRef.current.currentTime = (value / 100) * audioRef.current.duration;
    setProgress(value);
  };

  const handleVolume = (e) => {
    if (!audioRef.current) return;
    audioRef.current.volume = e.target.value;
  };

  return (
    <div className="flex flex-col items-center gap-4 bg-gray-900 text-white p-6 rounded-xl w-full max-w-md">
      {/* Audio */}
      <audio ref={audioRef} src="/assets/music/1.mp3" />

      <h2 className="text-lg font-semibold">Testing Song: 1.mp3</h2>

      {/* Progress Bar */}
      <input
        type="range"
        min="0"
        max="100"
        step="0.1"
        value={progress}
        onChange={handleSeek}
        className="w-full accent-green-500"
      />

      {/* Controls */}
      <div className="flex items-center gap-6 mt-2">
        <button
          onClick={togglePlay}
          className="w-14 h-14 flex items-center justify-center rounded-full bg-white text-black"
        >
          {isPlaying ? <Pause size={28} /> : <Play size={28} />}
        </button>
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
