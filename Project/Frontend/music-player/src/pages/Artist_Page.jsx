import axios from "axios";
import React, { useState, useEffect } from "react";
import "../index.css";
import Layout_Artist from "../components/Layout_Artist.jsx";
import Layout from "../components/Layout.jsx";
export default function Artist_Page() {
  const [lists, setList] = useState([]);
  const fetchArtists = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/library/artists");
      setList(response.data);
    } catch (error) {
      console.log("error", error);
    }
  };

  useEffect(() => {
    fetchArtists();
  }, []);

  return (
    <>
      <Layout>
        {lists.map((artist, artistIndex) => (
          <div key={artistIndex} className="mb-4">
            <Layout_Artist
              name={artist.name}
              image={artist.url}
              albums={artist.albums.map((album) => album.name)}
            />
          </div>
        ))}
      </Layout>
    </>

    // <div className="grid grid-cols-4 gap-4">
    //   {lists.map((artist, artistIndex) => (
    //     <div key={artistIndex}>
    //       <div>{artist.name}</div>
    //       <div>
    //         {artist.albums?.map((album, albumIndex) => (
    //           <span key={albumIndex}>{album.name} </span>
    //         ))}
    //       </div>
    //     </div>
    //   ))}
    // </div>
  );
}
