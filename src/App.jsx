// src/App.jsx
import { useState, useEffect } from "react";
import StartScreen from "./components/StartScreen";

function App() {
  const [started, setStarted] = useState(false);

  useEffect(() => {
    if (window.Telegram?.WebApp) {
      window.Telegram.WebApp.expand();
      window.Telegram.WebApp.ready();
    }
  }, []);

  return started ? (
    <div style={{ padding: 20 }}>📆 Тут будет календарь</div>
  ) : (
    <StartScreen onStart={() => setStarted(true)} />
  );
}

export default App;
