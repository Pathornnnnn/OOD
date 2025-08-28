import SongList from "../components/SongList.jsx";
import React, { useState, useEffect } from "react";
import axios from "axios";
import Layout from "../components/Layout.jsx";

export default function SongListPage({ artistId, albumId }) {
    const [songs, setSongs] = useState([]);
    const fetchSongs = async () => {
        try {
            const response = await axios.get(
                `http://127.0.0.1:8000/library/songs`
            );
            setSongs(response.data);
        } catch (error) {
            console.log("error", error);
        }
    };

    useEffect(() => {
        fetchSongs();
    }, []);
    const handleSelectSong = (song) => {
        console.log("Selected song:", song);
        // Implement play song logic here
    }
    return (
        <Layout>
            <h2 className="text-2xl font-bold mb-4">Song List</h2>
            <SongList songs={songs} onSelect={handleSelectSong} />
        </Layout>
    );
}