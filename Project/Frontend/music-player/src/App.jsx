import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
// import "./App.css";
import Artist_Page from "./pages/Artist_Page";
// import "./index.css";
import Player from "./components/MediaPlayerControls";
function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Artist_Page />
      <Player />
    </>
  );
}

export default App;
