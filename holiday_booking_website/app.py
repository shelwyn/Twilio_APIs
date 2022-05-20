from flask import Flask, render_template, request
import requests
import json
import pymongo
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)
url = "http://<YOUR API IP>/holiday" #This is the API URL to make calls and send sms with TWILIO, (This file is availailable in TWILIO_CALL_SMS folder

@app.route('/incident-management', methods=['GET', 'POST'])
def im():
	#https://account.mongodb.com/account   -- Get a free mongo DB here (This is used for the Incident management app)
    client = pymongo.MongoClient("mongodb+srv://<MONGO_DB_URL>:" + urllib.parse.quote("<MONGO_DB_PASSWORD>") + "@XXXXXX.XXXX.mongodb.net/IM?retryWrites=true&w=majority")
    db = client["IM"]	#Database Name
    collection = db["Incidents"]	#Collection Name
    records=""
    for x in collection.find():
        records += "<tr><td>" + str(x['user']) + "</td><td>" + str(x['Type']) + "</td><td>" + str(x['Incident']) + "</td></tr>"

    html='<div style="background-color:black">' \
         '<font color="white"><h2>Incidents</h2>' \
         '</font></div>' \
         '<br><hr><table border=1><tr bgcolor="yellow"><td><b>Requestor</b></td><td><b>ReqType</b></td><td><b>Incident </b></td></tr>' + str(records) + '</table>'
    return(html)


@app.route('/', methods=['GET', 'POST'])
def index():
    response_message="-"
    if request.method == 'POST':
        if request.form['submit_button'] == 'Send Booking Enquiry':
            payload={
                        "country": request.form['country'],
                        "members": request.form['members'],
                        "nights": request.form['nights']
                    }
            json_payload = json.dumps(payload)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=json_payload)
            response_message=response.text

    return render_template ("index.html",response_message=response_message)

#This microservice will run on port 3000 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
