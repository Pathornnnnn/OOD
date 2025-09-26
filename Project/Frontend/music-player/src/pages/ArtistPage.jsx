import axios from "axios";
import React, { useState, useEffect } from "react";
import Layout from "../components/Layout.jsx";
import ArtistCard from "../components/ArtistCard.jsx";

export default function ArtistPage() {
  const backendUrl = import.meta.env.VITE_BACKEND_URL;
  const [artists, setArtists] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchArtists = async () => {
    try {
      setLoading(true);
      const res = await axios.get(`${backendUrl}/library/artists`);
      setArtists(res.data);
    } catch (err) {
      console.error(err);
      setError("Failed to fetch artists.");
    } finally {
      setLoading(false);
    }
  };

  const handleAddSongToQueue = async (songId) => {
    try {
      await axios.post(`${backendUrl}/queue/add/${songId}`);
      console.log(`Song ${songId} added to queue.`);
    } catch (err) {
      console.error("Error adding song to queue:", err);
    }
  };

  useEffect(() => {
    fetchArtists();
  }, []);

  if (loading) return <Layout><p className="text-center">Loading...</p></Layout>;
  if (error) return <Layout><p className="text-center text-red-500">{error}</p></Layout>;

  return (
    <Layout>
      <div className="flex flex-col gap-8">
        {artists.map((artist) => (
          <ArtistCard
            key={artist.id}
            artist={artist}
            onAddSong={handleAddSongToQueue}
          />
        ))}
      </div>
    </Layout>
  );
}
