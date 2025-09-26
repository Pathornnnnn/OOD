import React, { useState, useEffect } from "react";
import axios from "axios";
import QueueDisplay from "../components/QueueDisplay.jsx";
import Layout from "../components/Layout.jsx";

export default function QueuePage() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  const [queue, setQueue] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);

  const fetchQueue = async () => {
    try {
      const response = await axios.get(`${backendUrl}/queue`);
      if (Array.isArray(response.data)) {
        setQueue(response.data);
      } else {
        console.error("Queue API response is not an array:", response.data);
        setQueue([]);
      }
    } catch (error) {
      console.error("Error fetching queue:", error);
      setQueue([]);
    }
  };

  const fetchCurrentSong = async () => {
    try {
      const response = await axios.get(`${backendUrl}/player/current`);
      setCurrentSong(response.data);
    } catch (error) {
      console.error("Error fetching current song:", error);
      setCurrentSong(null);
    }
  };

  useEffect(() => {
    fetchQueue();
    fetchCurrentSong();

    const interval = setInterval(() => {
      fetchQueue();
      fetchCurrentSong();
    }, 1000); // Refresh every second

    return () => clearInterval(interval);
  }, []);

  const currentSongId = currentSong ? currentSong.id : null;

  return (
    <Layout>
      <div className="bg-zinc-950 min-h-screen flex flex-col items-center justify-start p-6">
        <h1 className="text-3xl text-purple-400 font-bold mb-6">
          🎶 Music Queue
        </h1>
        <QueueDisplay queue={queue} currentSongId={currentSongId} />
      </div>
    </Layout>
  );
}
