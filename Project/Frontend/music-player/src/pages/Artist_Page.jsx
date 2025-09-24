import axios from "axios";
import React, { useState, useEffect } from "react";
import "../index.css";
import Layout_Artist from "../components/Layout_Artist.jsx";
import Layout from "../components/Layout.jsx";

export default function Artist_Page() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;
  console.log("Backend URL:", backendUrl);
  
  const [lists, setList] = useState([]);

  const fetchArtists = async () => {
    try {
      // Use the environment variable here
      const response = await axios.get(`${backendUrl}/library/artists`);
      setList(response.data);
    } catch (error) {
      console.log("error", error);
    }
  };

  const handleAddSongToQueue = async (songId) => {
    try {
      // Use the environment variable here
      await axios.post(`${backendUrl}/queue/add/${songId}`);
      console.log(`Song with ID ${songId} added to queue.`);
    } catch (error) {
      console.error("Error adding song to queue:", error);
    }
  };

  useEffect(() => {
    fetchArtists();
  }, []);

  return (
    <>
      <Layout>
        <div className="flex flex-col gap-8">
          {lists.map((artist) => (
            <Layout_Artist
              key={artist.id}
              artist={artist}
              onAddSong={handleAddSongToQueue}
            />
          ))}
        </div>
      </Layout>
    </>
  );
}