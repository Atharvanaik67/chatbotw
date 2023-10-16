from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Hi')
    msg = request.form.get('What are the Cources Avilabel in Computer Science Department')


    # Create reply
    resp = MessagingResponse()
    resp.message("Hello Welcome to Fergusson College".format(msg)) 
    resp.message("This is Computer Science Department".format(msg))  
    resp.message("In PG Section There Are Three Cources Avilable".format(msg)) 
    resp.message("1. MSc(Computer Science) 2. MSc(Computer Application) 3.MSc(Data Science)".format(msg)) 


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)