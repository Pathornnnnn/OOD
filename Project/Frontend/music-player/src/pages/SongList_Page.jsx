import SongList from "../components/SongList.jsx";
import React, { useState, useEffect } from "react";
import axios from "axios";
import Layout from "../components/Layout.jsx";

const backendUrl = import.meta.env.VITE_BACKEND_URL;

export default function SongListPage({ artistId, albumId }) {
    const [songs, setSongs] = useState([]);
    
    // Function to fetch songs based on artist or album
    const fetchSongs = async () => {
        let apiUrl = `${backendUrl}/library/songs`;

        if (artistId) {
            apiUrl = `${backendUrl}/library/artists/${artistId}/songs`;
        } else if (albumId) {
            apiUrl = `${backendUrl}/library/albums/${albumId}/songs`;
        }
        
        try {
            const response = await axios.get(apiUrl);
            setSongs(response.data);
        } catch (error) {
            console.error("Error fetching songs:", error);
        }
    };

    useEffect(() => {
        fetchSongs();
    }, [artistId, albumId]); // Re-run effect when artistId or albumId changes

    const handleSelectSong = (song) => {
        console.log("Selected song:", song);
        // Implement play song logic here
    };

    // Determine the title based on the props
    const pageTitle = artistId 
        ? "Artist Songs" 
        : albumId 
        ? "Album Songs" 
        : "All Songs";

    return (
        <Layout>
            <h2 className="text-2xl font-bold mb-4">{pageTitle}</h2>
            <SongList songs={songs} onSelect={handleSelectSong} />
        </Layout>
    );
}