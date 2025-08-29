import { StrictMode } from "react";
import { createRoot } from "react-dom/client"; // ✅ ใช้ createRoot
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home_Page from "./pages/Home_Page.jsx";
import Artist_Page from "./pages/Artist_Page.jsx";
import SongListPage from "./pages/SongList_Page.jsx";
// Router ตัวอย่าง
const router = createBrowserRouter([
  { path: "/", element: <Home_Page /> },
  {
    path: "/app",
    element: <Home_Page />,
  },
  {
    path: "/Artist",
    element: <Artist_Page />,
  },
  {
    path: "/SongList",
    element: <SongListPage />,
  },
]);

// ใช้ createRoot ที่ import มาโดยตรง
createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
