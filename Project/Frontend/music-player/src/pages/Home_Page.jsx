import Layout from "../components/Layout";
import MusicPlayerSingle from "../components/PlayerSingle";
import "../index.css";

export default function Home_Page() {
  return (
    <Layout>
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900">
        <div className="text-white text-3xl font-bold mb-4">
          Welcome to Music Player
        </div>
        <div className="text-gray-400 text-lg mb-8 text-center">
          Your personal music library at your fingertips
        </div>
        {/* Music Player */}
        <div className="w-full max-w-md">
          <MusicPlayerSingle />
        </div>
      </div>
    </Layout>
  );
}
