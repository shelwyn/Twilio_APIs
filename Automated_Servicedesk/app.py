from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import random
import pymongo
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)


@app.route("/software", methods=['GET', 'POST'])
def software():
    resp = VoiceResponse()
    resp_secondary = VoiceResponse()
    request_from = request.values['From']
    #https://account.mongodb.com/account   -- Get a free mongo DB here (This is used for the Incident management app)
    client = pymongo.MongoClient("mongodb+srv://<MONGO_DB_URL>:" + urllib.parse.quote("<MONGO_DB_PASSWORD>") + "@XXXXXX.XXXX.mongodb.net/IM?retryWrites=true&w=majority")
    db = client["IM"] #Database Name
    collection = db["Incidents"]  #Collection Name
    INC = random.randint(1111,9999)
    if 'Digits' in request.values:
        choice = request.values['Digits']
        INC = random.randint(1111,9999)
        if choice == '1':
            resp.say('A technician will contact you soon for the installation request, your incident number is:' + str(INC))
            record = {"user": str(request_from),"Incident": str(INC),"Type": "Software Installation"}
            add_one = collection.insert_one(record)
            return str(resp)
        elif choice == '2':
            record = {"user": str(request_from),"Incident": str(INC),"Type": "Software Configuration"}
            add_one = collection.insert_one(record)
            resp.say('A technician will contact you soon for the configuration request, your incident number is:' + str(INC))
        else:
            resp.say("Sorry, I don't understand that choice.")

    gather = Gather(num_digits=1)
    gather.say('Press 1 for installing a new software. Press 2 for configuration of an existing software')
    resp.append(gather)

    return str(resp)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()
    resp_secondary = VoiceResponse()
    request_from = request.values['From']
    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']
        # <Say> a different message depending on the caller's choice
        INC = random.randint(1111,9999)
        if choice == '1':
            resp.say('Please visit your nearest office with the hardware you are calling for, your incident number is:' + str(INC))
            return str(resp)
        elif choice == '2':
            resp.redirect('/software')
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # Start our <Gather> verb
    gather = Gather(num_digits=1)
    gather.say('Press 1 for hardware. Press 2 for software')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

