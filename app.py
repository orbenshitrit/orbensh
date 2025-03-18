from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "my_secure_token"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        challenge = request.args.get("hub.challenge")
        verify_token = request.args.get("hub.verify_token")

        if verify_token == VERIFY_TOKEN:
            return challenge, 200  
        return "Unauthorized", 403

    if request.method == "POST":
        data = request.json
        print("📩 קיבלנו הודעה מה-WhatsApp API:", data)
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
