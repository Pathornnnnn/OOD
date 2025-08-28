// Layout.jsx
import React from "react";

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col">
      {/* Header */}
      <header className="bg-gradient-to-r from-purple-700 via-black to-purple-700 p-4 shadow-lg">
        <h1 className="text-2xl font-extrabold tracking-wider text-center text-purple-300 glow-text">
          🎤 Rapper Music Player
        </h1>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-6">{children}</main>

      {/* Footer */}
      <footer className="bg-gray-900 text-center p-3 text-sm border-t border-purple-500">
        <p className="text-purple-400">© 2025 Rapper Vibes Music</p>
      </footer>
    </div>
  );
};

export default Layout;
