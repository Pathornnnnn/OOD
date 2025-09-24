import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from '../components/Layout.jsx';
import MediaPlayerControls from '../components/MediaPlayerControls'; 
import "../index.css";

export default function Home_Page() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;
  console.log("Backend URL:", backendUrl);

  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [currentSong, setCurrentSong] = useState(null);
  const [totalDuration, setTotalDuration] = useState(0);

  // Function: Fetch ข้อมูลเพลงปัจจุบันจาก API
  const fetchCurrentSong = async () => {
    try {
      const response = await axios.get(`${backendUrl}/player/current`);
      if (response.data) {
        setCurrentSong(response.data);
        setCurrentTime(response.data.currentTime || 0);
        setTotalDuration(response.data.duration);
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

  // Handler: ควบคุมการเล่น/หยุดเพลง
  const handlePlayPause = async () => {
    try {
      const endpoint = isPlaying ? '/pause' : '/play';
      await axios.post(`${backendUrl}/player${endpoint}`);
      await fetchCurrentSong();
    } catch (error) {
      console.error("Error toggling play/pause:", error);
    }
  };

  // Handler: ข้ามไปเพลงถัดไป
  const handleNext = async () => {
    try {
      await axios.post(`${backendUrl}/player/next`);
      await fetchCurrentSong();
    } catch (error) {
      console.error("Error skipping to next track:", error);
    }
  };

  // Handler: ย้อนกลับไปเพลงก่อนหน้า
  const handlePrevious = async () => {
    try {
      await axios.post(`${backendUrl}/player/previous`);
      await fetchCurrentSong();
    } catch (error) {
      console.error("Error skipping to previous track:", error);
    }
  };

  // Effect: Fetch ข้อมูลครั้งแรกและอัปเดตทุกวินาที
  useEffect(() => {
    fetchCurrentSong();

    const interval = setInterval(() => {
      if (isPlaying) {
        setCurrentTime(prevTime => prevTime + 1);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [isPlaying]);

  return (
    <Layout>
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900">
        <div className="text-white text-3xl font-bold mb-4">
          Welcome to Music Player
        </div>
        <div className="text-gray-400 text-lg mb-8 text-center">
          Your personal music library at your fingertips
        </div>
        <div className="w-full max-w-md">
          <MediaPlayerControls 
            currentSong={currentSong}
            isPlaying={isPlaying}
            currentTime={currentTime}
            totalDuration={totalDuration}
            onPlayPause={handlePlayPause}
            onNext={handleNext}
            onPrevious={handlePrevious}
            // Add other handlers here
          />
        </div>
      </div>
    </Layout>
  );
}