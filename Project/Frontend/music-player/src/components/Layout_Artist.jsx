// Layout_Artist.jsx
import React from "react";

const Layout_Artist = ({ name, albums, image }) => {
  return (
    <div className="bg-gradient-to-r from-black via-gray-900 to-black text-white p-6 rounded-2xl shadow-lg border border-purple-500 hover:shadow-[0_0_20px_#8b5cf6] transition">
      <div className="flex items-center space-x-4">
        {/* artist image */}
        <img
          src={image}
          alt={name}
          className="w-16 h-16 rounded-full border-2 border-purple-500 shadow-md"
        />

        {/* artist name + albums */}
        <div>
          <h2 className="text-2xl font-extrabold tracking-wide text-purple-400 text-left">
            {name}
          </h2>
          <div className="flex flex-wrap gap-2 mt-2">
            {albums.map((album, idx) => (
              <span
                key={idx}
                className="px-3 py-1 text-sm rounded-full bg-gray-800 border border-purple-500 hover:bg-purple-600 hover:shadow-[0_0_10px_#8b5cf6] cursor-pointer transition"
              >
                {album}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Layout_Artist;
