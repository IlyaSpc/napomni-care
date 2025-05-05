import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
import requests

# === CONFIG ===
TELEGRAM_BOT_TOKEN = "7956554161:AAFhy7lY7sXbm863aizX-oVo0ucQ9UoFspM"
SPREADSHEET_NAME = "Напомни App"  # Пример: Напоминания
CHECK_INTERVAL_SECONDS = 60  # проверять каждую минуту

# === Авторизация Google Sheets ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).sheet1

# === Отправка сообщений в Telegram
def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=data)

# === Проверка и отправка напоминаний
def check_reminders():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    expected_headers = ["telegram_id", "date", "time", "text", "notified"]
    data = sheet.get_all_records(expected_headers=expected_headers)

    for i, row in enumerate(data, start=2):  # строка 1 — заголовки
        date = row.get("date")
        time_ = row.get("time")
        full_datetime = f"{date} {time_}"
        notified = str(row.get("notified")).lower() == "true"

        if full_datetime == now and not notified:
            message = row.get("text")
            chat_id = row.get("telegram_id")

            print(f"⏰ Напоминаю: {message} → {chat_id}")
            send_telegram_message(chat_id, f"🔔 Напоминание: {message}")
            sheet.update_cell(i, 5, "TRUE")  # Обновляем notified → TRUE

# === Запуск цикла
print("📡 Notifier запущен...")

while True:
    check_reminders()
    time.sleep(CHECK_INTERVAL_SECONDS)
