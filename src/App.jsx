import { useEffect, useState } from 'react';
import StartScreen from './components/StartScreen';

function App() {
  const [telegramUser, setTelegramUser] = useState(null);

  useEffect(() => {
    const tg = window.Telegram?.WebApp;

    if (tg) {
      tg.ready(); // уведомить Telegram, что мы готовы
      const user = tg.initDataUnsafe?.user;

      console.log('📦 Telegram WebApp:', tg);
      console.log('🙋 Пользователь из initData:', user);

      if (user) {
        setTelegramUser(user);
      } else {
        console.warn('⚠️ Нет данных о пользователе!');
      }
    } else {
      console.warn('🚫 Telegram WebApp API недоступен!');
    }
  }, []);

  return (
    <div>
      {telegramUser ? (
        <StartScreen telegramUser={telegramUser} />
      ) : (
        <div style={{ padding: '3rem', textAlign: 'center', fontFamily: 'sans-serif' }}>
          <h1>Напомни мне</h1>
          <p>⏳ Получаем данные пользователя из Telegram...</p>
        </div>
      )}
    </div>
  );
}

export default App;
