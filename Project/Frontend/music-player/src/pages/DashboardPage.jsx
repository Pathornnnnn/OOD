import React, { useState, useEffect } from "react";
import axios from "axios";
import Layout from "../components/Layout.jsx";
import MediaPlayerControls from "../components/MediaPlayerControls.jsx";
import QueueDisplay from "../components/QueueDisplay.jsx";
import HistoryDisplay from "../components/HistoryDisplay.jsx";

export default function DashboardPage() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  const [queue, setQueue] = useState([]);
  const [history, setHistory] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [totalDuration, setTotalDuration] = useState(0);

  // Fetch functions
  const fetchQueue = async () => {
    try {
      const response = await axios.get(`${backendUrl}/queue`);
      setQueue(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error("Error fetching queue:", error);
      setQueue([]);
    }
  };

  const fetchHistory = async () => {
    try {
      const response = await axios.get(`${backendUrl}/history`);
      setHistory(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error("Error fetching history:", error);
      setHistory([]);
    }
  };

  const fetchCurrentSong = async () => {
    try {
      const response = await axios.get(`${backendUrl}/player/current`);
      if (response.data) {
        setCurrentSong(response.data);
        setCurrentTime(response.data.currentTime || 0);
        setTotalDuration(response.data.duration || 0);
        setIsPlaying(response.data.isPlaying || false);
      } else {
        setCurrentSong(null);
        setCurrentTime(0);
        setTotalDuration(0);
        setIsPlaying(false);
      }
    } catch (error) {
      console.error("Error fetching current song:", error);
    }
  };

  // Player handlers
  const handlePlayPause = async () => {
    try {
      const endpoint = isPlaying ? "/pause" : "/play";
      await axios.post(`${backendUrl}/player${endpoint}`);
      await fetchCurrentSong();
    } catch (error) {
      console.error("Error toggling play/pause:", error);
    }
  };

  const handleNext = async () => {
    try {
      await axios.post(`${backendUrl}/player/next`);
      await fetchCurrentSong();
      fetchQueue();
      fetchHistory();
    } catch (error) {
      console.error("Error skipping to next:", error);
    }
  };

  const handlePrevious = async () => {
    try {
      await axios.post(`${backendUrl}/player/previous`);
      await fetchCurrentSong();
      fetchQueue();
      fetchHistory();
    } catch (error) {
      console.error("Error skipping to previous:", error);
    }
  };

  // Queue add
  const handleAddSongToQueue = async (songId) => {
    try {
      await axios.post(`${backendUrl}/queue/add/${songId}`);
      fetchQueue();
    } catch (error) {
      console.error("Error adding song to queue:", error);
    }
  };

  useEffect(() => {
    fetchQueue();
    fetchHistory();
    fetchCurrentSong();

    const interval = setInterval(() => {
      if (isPlaying) setCurrentTime((prev) => prev + 1);
      fetchQueue();
      fetchHistory();
      fetchCurrentSong();
    }, 1000);

    return () => clearInterval(interval);
  }, [isPlaying]);

  const currentSongId = currentSong ? currentSong.id : null;

  return (
    <Layout>
      <div className="bg-zinc-950 min-h-screen flex flex-col items-center p-6 space-y-8">
        {/* Player Controls */}
        <MediaPlayerControls
          currentSong={currentSong}
          isPlaying={isPlaying}
          currentTime={currentTime}
          totalDuration={totalDuration}
          onPlayPause={handlePlayPause}
          onNext={handleNext}
          onPrevious={handlePrevious}
        />

        {/* Queue + History */}
        <div className="flex flex-col md:flex-row gap-8 w-full max-w-6xl">
          <QueueDisplay queue={queue} currentSongId={currentSongId} />
          <HistoryDisplay history={history} currentSongId={currentSongId} />
        </div>

        {/* Example: Add song buttons (simulate ArtistPage interaction) */}
        <div className="bg-zinc-900 p-4 rounded-lg shadow-xl w-full max-w-4xl">
          <h2 className="text-white font-bold text-xl mb-2">
            🎶 Add Songs to Queue (Example)
          </h2>
          <div className="flex flex-wrap gap-2">
            {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14].map((id) => (
              <button
                key={id}
                onClick={() => handleAddSongToQueue(id)}
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
