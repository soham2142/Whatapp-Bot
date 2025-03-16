from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if "hello" in incoming_msg:
        msg.body("Hello! I'm your AI finance assistant. Send 'track' to log an expense.")
    elif "track" in incoming_msg:
        msg.body("Please enter your expense in this format: \nAmount - Category (e.g., 500 - Food)")
    else:
        msg.body("I didn't understand that. Type 'help' for options.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
