# Twilio_APIs
Twilio communication API's, inbound/outbound calls, SMS

Instructions for sample, creating incident with automated service desk

1 - Get a Twilio trial account: https://www.twilio.com/ | https://account.mongodb.com/account   -- Get a free mongo DB here (This is used for the Incident management         app)
2 - Get a Twilio number (once you login, go to the section Voice, try it out) to get a new number
3 - Confirm programming language as Python
4 - Run the python file (app.py) in the folder (Automated_Servicedesk), if you are running it on a cloud instance, you will have to use the instance public ip with port     5000. If you are running it on your local machine, you will have to tunnel it with NGROK (port 5000), once the microservice is up, Go to Twilio console, click on 
    Phone Numbers, click Manage, click Active numbers, click on your assigned number, scroll down to section "A call comes in" select Webhook add the address 
    http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>/voice or (http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>:5000/voice), select method as HTTP POST. click Save
5 - Run the python file in the folder holiday_booking_website (this file also contains code to read data from the mongo DB) and show it on the Incident Management portal
    if you are running it on a cloud instance, you will have to use the instance public ip with port 3000. If you are running it on your local machine, you will have         to tunnel it with NGROK (port 3000). you can get the portal up by opening up tttp://<YOUR_PYTHON_GENERATED_IP_ADDRESS>/  or                                               (http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>:3000/voice)
6 - Dial your Twilio number, follow instructions, the application will create an entry in the Mongo DB, refresh the IM portal page and you should see the Mongo DB entry
    
