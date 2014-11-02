from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls with a simple text message."""
	resp = twilio.twiml.Response()
	resp.message("Hello Pam")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)

#from twilio.rest import TwilioRestClient
#account = "ACf10261d794fdaf920c6e1b08908cf198"
#token = "935387730b05191917e9773e8b03d0dd"
#client = TwilioRestClient(account, token)
#message = client.messages.create(to="+16463877470", from_="+13473703263", body="Hello world")
