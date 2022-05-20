# Twilio_APIs
Twilio communication API's, inbound/outbound calls, SMS

==================================================================================================================================

Instructions for sample, creating incident with automated service desk

==================================================================================================================================

![alt text](https://github.com/shelwyn/Twilio_APIs/blob/main/images/Twilio%20Call%20with%20Inputs.PNG)

1 - Get a Twilio trial account: https://www.twilio.com/ | -- Get a free mongo DB here: https://account.mongodb.com/account 

2 - Get a Twilio number (once you login, go to the section Voice, try it out) to get a new number

3 - Confirm programming language as Python

4 - Run the python file (app.py) in the folder (Automated_Servicedesk), if you are running it on a cloud instance, you will have to use the instance public ip with port     5000. If you are running it on your local machine, you will have to tunnel it with NGROK (port 5000), once the microservice is up, Go to Twilio console, click on 
    Phone Numbers, click Manage, click Active numbers, click on your assigned number, scroll down to section "A call comes in" select Webhook add the address 
    http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>/voice or (http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>:5000/voice), select method as HTTP POST. click Save
    
5 - Run the python file in the folder holiday_booking_website (this file also contains code to read data from the mongo DB) and show it on the Incident Management portal
    if you are running it on a cloud instance, you will have to use the instance public ip with port 3000. If you are running it on your local machine, you will have         to tunnel it with NGROK (port 3000). you can get the portal up by opening up htttp://<YOUR_PYTHON_GENERATED_IP_ADDRESS>/incident-management  or                           (http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>:3000/incident-management)
    
6 - Dial your Twilio number, follow instructions, the application will create an entry in the Mongo DB, refresh the IM portal page and you should see the Mongo DB entry
    
================================================================================================================================== 

Instructions for sample booking holiday package

==================================================================================================================================

![alt text](https://github.com/shelwyn/Twilio_APIs/blob/main/images/Twilio%20SMS%20Call.PNG)

1 - Run the python file (app.py) in the folder TWILIO_CALL_SMS (update account_sid, auth_token, to [phone number], from [phone number]) you get from Twilio. if you are       running it on a cloud instance, you will have to use the instance public ip with port 80. If you are running it on your local machine, you will have to tunnel it         with NGROK (port 80)

2 - Update the "url" variable in the file holiday_booking_website/app.py to the ip address ex: http://<YOUR API IP>/holiday (from point 1) and re-start the app.py. you       can now load the holiday booking website by typing the IP address. (If you are running it on your local machine, you will have to tunnel it with NGROK (port 3000).       you can get the portal up by opening up htttp://<YOUR_PYTHON_GENERATED_IP_ADDRESS>/ or (http://<YOUR_PYTHON_GENERATED_IP_ADDRESS>:3000/
    
3 - Select the fields and click on Submit, you should get a call and and SMS from the API. 
