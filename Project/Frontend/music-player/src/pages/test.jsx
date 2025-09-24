import React, { useState, useEffect } from "react";
import axios from "axios";
import QueueDisplay from "../components/QueueDisplay";

const App = () => {
  // Get the backend URL from the environment variable
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  const [queue, setQueue] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);

  const fetchQueue = async () => {
    try {
      const response = await axios.get(`${backendUrl}/queue`);
      if (Array.isArray(response.data)) {
        setQueue(response.data);
      } else {
        console.error("API response for queue is not an array:", response.data);
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
  }, []);

  const currentSongId = currentSong ? currentSong.id : null;

  return (
    <div className="bg-zinc-950 min-h-screen flex items-center justify-center p-4">
      <QueueDisplay queue={queue} currentSongId={currentSongId} />
    </div>
  );
};

export default App;