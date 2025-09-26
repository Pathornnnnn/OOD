import { StrictMode } from "react";
import { createRoot } from "react-dom/client"; // ✅ ใช้ createRoot
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import HomePage from "./pages/HomePage";
import ArtistPage from "./pages/ArtistPage";
import HistoryDisplay from "./components/HistoryDisplay";
import DashboardPage from "./pages/DashboardPage";
import HistoryPage from "./pages/HistoryPage";

// Router ตัวอย่าง
const router = createBrowserRouter([
  { path: "/", element: <HomePage /> },
  {
    path: "/artists",
    element: <ArtistPage />,
  },
  {
    path: "/dashboard",
    element: <DashboardPage />,
  },
  {
    path: "/history",
    element: <HistoryPage />,
  },
]);

// ใช้ createRoot ที่ import มาโดยตรง
createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
