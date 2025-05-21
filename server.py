from flask import Flask, request, send_from_directory
import requests
import json

app = Flask(__name__)

ADMIN_CHAT_ID = "7480356744"
BOT_TOKEN = "7793773933:AAEGuW-ZKZH6MG8AhmyD28ySA88UlnwQirE"
PASSWORD = "22"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/alarm.mp3')
def alarm_sound():
    return send_from_directory('.', 'alarm.mp3')

@app.route('/log', methods=['POST'])
def log_visitor():
    data = request.json
    msg = f"Alarm triggered!\nUser-Agent: {data.get('userAgent')}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                 params={"chat_id": ADMIN_CHAT_ID, "text": msg})
    return 'Logged'

@app.route('/unlock', methods=['POST'])
def unlock():
    data = request.json
    code = data.get("code")
    if code == PASSWORD:
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                     params={"chat_id": ADMIN_CHAT_ID, "text": "Device unlocked with correct password."})
    else:
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                     params={"chat_id": ADMIN_CHAT_ID, "text": "Incorrect unlock attempt."})
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
