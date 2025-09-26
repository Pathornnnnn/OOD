import React from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import "../index.css";
export default function HomePage() {
  const navigate = useNavigate();

  const sections = [
    { label: "🎤 Artists", path: "/artists" },
    { label: "▶️ Queue", path: "/dashboard" },
    { label: "📋 History", path: "/history" },
  ];

  return (
    <Layout>
      <div className="min-h-screen flex flex-col items-center justify-center bg-zinc-950 text-white p-6 space-y-10">
        <h1 className="text-5xl font-extrabold text-purple-400">
          🎵 Music OOD Player
        </h1>
        <p className="text-gray-400 text-lg text-center max-w-xl">
          Welcome! Navigate to different sections to explore Artists, Queue,
          History, and your Media Player.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-3xl">
          {sections.map((section) => (
            <button
              key={section.path}
              onClick={() => navigate(section.path)}
              className="bg-purple-600 hover:bg-purple-700 transition-colors px-6 py-4 rounded-xl shadow-xl text-white font-bold text-lg"
            >
              {section.label}
            </button>
          ))}
        </div>
      </div>
    </Layout>
  );
}
