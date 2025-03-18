import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# קבלת משתני סביבה מ-Render
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "my_secure_token")  # טוקן לאימות ה-Webhook
WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # אימות מול ה-Webhook של WhatsApp
        challenge = request.args.get("hub.challenge")
        verify_token = request.args.get("hub.verify_token")

        if verify_token == VERIFY_TOKEN:
            return challenge, 200  
        return "Unauthorized", 403

    if request.method == "POST":
        # קבלת הודעות נכנסות
        data = request.json
        print("📩 קיבלנו הודעה מה-WhatsApp API:", data)
        return jsonify({"status": "received"}), 200

@app.route("/")
def home():
    return "WhatsApp Bot is running!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # שימוש בערך של PORT מ-Render
    app.run(host="0.0.0.0", port=port)


