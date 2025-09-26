import React, { useState, useEffect } from "react";
import axios from "axios";
import HistoryDisplay from "../components/HistoryDisplay.jsx";
import Layout from "../components/Layout.jsx";

export default function HistoryPage() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  const [history, setHistory] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);

  const fetchHistory = async () => {
    try {
      const response = await axios.get(`${backendUrl}/history`);
      if (Array.isArray(response.data)) {
        setHistory(response.data);
      } else {
        console.error("History API response is not an array:", response.data);
        setHistory([]);
      }
    } catch (error) {
      console.error("Error fetching history:", error);
      setHistory([]);
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
    fetchHistory();
    fetchCurrentSong();

    const interval = setInterval(() => {
      fetchHistory();
      fetchCurrentSong();
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const currentSongId = currentSong ? currentSong.id : null;

  return (
    <Layout>
      <div className="bg-zinc-950 min-h-screen flex flex-col items-center justify-start p-6">
        <h1 className="text-3xl text-green-400 font-bold mb-6">
          🗂️ Playback History
        </h1>
        <HistoryDisplay history={history} currentSongId={currentSongId} />
      </div>
    </Layout>
  );
}
