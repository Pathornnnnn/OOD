import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import Layout from "../components/Layout.jsx";
import MediaPlayerControls from "../components/MediaPlayerControls.jsx";
import QueueDisplay from "../components/QueueDisplay.jsx";
import HistoryDisplay from "../components/HistoryDisplay.jsx";

export default function DashboardPage() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  // ---------------- State ----------------
  const [queue, setQueue] = useState([]);
  const [history, setHistory] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [totalDuration, setTotalDuration] = useState(0);
  const [isLooping, setIsLooping] = useState(false);

  const [volume, setVolume] = useState(100);
  const [isMuted, setIsMuted] = useState(false);

  const audioRef = useRef(null);
  const autoNextRef = useRef(false); // ป้องกัน next ซ้ำ

  // ---------------- Fetch ----------------
  const fetchQueue = async () => {
    try {
      const res = await axios.get(`${backendUrl}/queue`);
      setQueue(Array.isArray(res.data) ? res.data : []);
    } catch (e) {
      console.error(e);
      setQueue([]);
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await axios.get(`${backendUrl}/history`);
      setHistory(Array.isArray(res.data) ? res.data : []);
    } catch (e) {
      console.error(e);
      setHistory([]);
    }
  };

  const fetchCurrentSong = async () => {
    try {
      const res = await axios.get(`${backendUrl}/player/current`);
      if (res.data) {
        setCurrentSong(res.data);
        setCurrentTime(res.data.currentTime || 0);
        setTotalDuration(res.data.duration || 0);
        setIsPlaying(res.data.isPlaying || false);
      } else {
        setCurrentSong(null);
        setCurrentTime(0);
        setTotalDuration(0);
        setIsPlaying(false);
      }
    } catch (e) {
      console.error(e);
    }
  };

  // ---------------- Controls ----------------
  const handlePlayPause = async () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
      setIsPlaying(false);
    } else {
      await audioRef.current.play();
      setIsPlaying(true);
    }
  };

  const handleNext = async () => {
    await axios.post(`${backendUrl}/player/next`);
    await fetchCurrentSong();
    fetchQueue();
    fetchHistory();
  };

  const handlePrevious = async () => {
    await axios.post(`${backendUrl}/player/previous`);
    await fetchCurrentSong();
    fetchQueue();
    fetchHistory();
  };

  const handleToggleLoop = async () => {
    const res = await axios.post(`${backendUrl}/player/toggle_loop`);
    setIsLooping(res.data.loop);
  };

  const handleSeek = (time) => {
    if (audioRef.current) {
      audioRef.current.currentTime = time;
      setCurrentTime(time);
    }
  };

  const handleToggleMute = () => {
    if (audioRef.current) {
      const newMuted = !isMuted;
      audioRef.current.muted = newMuted;
      setIsMuted(newMuted);
    }
  };

  const handleSetVolume = (newVolume) => {
    if (audioRef.current) {
      audioRef.current.volume = newVolume / 100;
      setVolume(newVolume);
      if (newVolume > 0) setIsMuted(false);
    }
  };

  // ---------------- Effects ----------------
  useEffect(() => {
    fetchQueue();
    fetchHistory();
    fetchCurrentSong();
  }, []);

  // Sync audio element
  useEffect(() => {
    const audio = audioRef.current;
    if (!audio || !currentSong) return;

    audio.src = `/assets/music/${currentSong.id}.mp3`;
    audio.loop = isLooping;
    audio.volume = volume / 100;
    audio.muted = isMuted;

    if (isPlaying) {
      audio.play().catch((e) => console.warn("Autoplay blocked:", e));
    }
  }, [currentSong, isPlaying, isLooping, volume, isMuted]);

  // Auto next เมื่อเพลงจบ
  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const updateTime = () => setCurrentTime(audio.currentTime);
    const updateDuration = () => setTotalDuration(audio.duration || 0);

    const handleEnded = async () => {
      if (autoNextRef.current) return;
      autoNextRef.current = true;
      await handleNext();
      autoNextRef.current = false;
    };

    audio.addEventListener("timeupdate", updateTime);
    audio.addEventListener("loadedmetadata", updateDuration);
    audio.addEventListener("ended", handleEnded);

    return () => {
      audio.removeEventListener("timeupdate", updateTime);
      audio.removeEventListener("loadedmetadata", updateDuration);
      audio.removeEventListener("ended", handleEnded);
    };
  }, [currentSong]);

  const currentIndex = currentSong ? currentSong.index : -1;
  const currentSongId = currentSong ? currentSong.id : null;

  return (
    <Layout>
      <div className="bg-zinc-950 min-h-screen flex flex-col items-center p-6 space-y-8">
        {/* Hidden audio */}
        <audio ref={audioRef} />

        {/* Player Controls */}
        <MediaPlayerControls
          currentSong={currentSong}
          isPlaying={isPlaying}
          currentTime={currentTime}
          totalDuration={totalDuration}
          onPlayPause={handlePlayPause}
          onNext={handleNext}
          onPrevious={handlePrevious}
          onSeek={handleSeek}
          onToggleLoop={handleToggleLoop}
          isLooping={isLooping}
          volume={volume}
          isMuted={isMuted}
          onSetVolume={handleSetVolume}
          onToggleMute={handleToggleMute}
        />

        {/* Queue + History */}
        <div className="flex flex-col md:flex-row gap-8 w-full max-w-6xl">
          <QueueDisplay queue={queue} currentIndex={currentIndex} />
          <HistoryDisplay
            history={history}
            currentSongId={currentSongId}
            onUndo={async () => {
              await axios.post(`${backendUrl}/history/undo`);
              fetchQueue();
              fetchHistory();
              fetchCurrentSong();
            }}
            onRedo={async () => {
              await axios.post(`${backendUrl}/history/redo`);
              fetchQueue();
              fetchHistory();
              fetchCurrentSong();
            }}
          />
        </div>

        {/* Add Songs Example */}
        <div className="bg-zinc-900 p-4 rounded-lg shadow-xl w-full max-w-4xl">
          <h2 className="text-white font-bold text-xl mb-2">
            🎶 Add Songs to Queue
          </h2>
          <div className="flex flex-wrap gap-2">
            {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((id) => (
              <button
                key={id}
                onClick={async () => {
                  await axios.post(`${backendUrl}/queue/add/${id}`);
                  fetchQueue();
                  fetchCurrentSong();
                }}
                className="bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700 transition"
              >
                Add Song {id}
              </button>
            ))}
          </div>
        </div>
      </div>
    </Layout>
  );
}
