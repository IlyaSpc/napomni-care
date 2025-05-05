import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [tgData, setTgData] = useState(null);

  useEffect(() => {
    const initData = window.Telegram?.WebApp?.initDataUnsafe;

    if (initData && initData.user) {
      setTgData(initData.user);
    } else {
      setTgData(null);
    }
  }, []);

  return (
    <div className="app-container">
      <h1>Напомни мне</h1>
      {tgData ? (
        <>
          <p>👤 Telegram ID: {tgData.id}</p>
          <p>Добро пожаловать, {tgData.first_name}!</p>
        </>
      ) : (
        <p>⌛ Получаем данные пользователя из Telegram...</p>
      )}
    </div>
  );
}

export default App;
