from flask import Flask, request, jsonify
from twilio.rest import Client
import time
app = Flask(__name__)

account_sid = '<TWILIO_SID>'
auth_token = '<TWILIO_AUTH_TOKEN>'
client = Client(account_sid, auth_token)


@app.route('/holiday', methods=['POST'])
def holiday():
    content = request.get_json(silent=True)
    complete_text=str(content['country']) + ' - ' + str(content['members']) + ' persons - ' + str(content['nights']) + ' nights'

    call = client.calls.create(
                        twiml='<Response><Say>A new holiday was booked on the website, please check your SMS for more details</Say></Response>',
                        to='+919620214631',
                        from_='+19706276412'
                    )

    time.sleep(5)

    message = client.messages.create(
    to="+<YOUR_PHONE_NO_RESISTERED_ON_TWILIO>",
    from_="+<YOUR_NUMBER_ASSIGNED_BY_TWILIO>",
    body=complete_text)

    return 'notified'

 #This microservice runs on port 80 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
