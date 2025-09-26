import React from "react";
import AlbumCard from "./AlbumCard.jsx";

const ArtistCard = ({ artist, onAddSong }) => {
  if (!artist) return <div>No artist data</div>;

  const { name, url, albums } = artist;

  return (
    <div className="bg-zinc-950 p-8 rounded-3xl shadow-2xl border border-gray-800 text-white max-w-4xl mx-auto">
      {/* Artist Info */}
      <div className="flex flex-col md:flex-row items-center md:space-x-8 mb-8 pb-8 border-b border-gray-700">
        <img
          src={url}
          alt={name}
          className="w-32 h-32 rounded-full border-4 border-purple-500 shadow-xl mb-4 md:mb-0"
        />
        <div className="text-center md:text-left">
          <h1 className="text-4xl font-extrabold text-purple-400">{name}</h1>
          <p className="text-lg text-gray-400 mt-1">
            Explore their discography below.
          </p>
        </div>
      </div>

      {/* Albums */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {albums.length > 0 ? (
          albums.map((album) => (
            <AlbumCard key={album.id} album={album} onAddSong={onAddSong} />
          ))
        ) : (
          <p className="text-center text-gray-500 italic col-span-2">No albums.</p>
        )}
      </div>
    </div>
  );
};

export default ArtistCard;
