from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
import os
from groq import Groq
import requests
print(os.getenv("GROQ_API_KEY"))


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Groq(api_key=GROQ_API_KEY)
twilio_client = Client(account_sid, auth_token)

@csrf_exempt
def send_whatsapp_message(request):
    print(request.POST)
    message = request.POST['Body']
    sender_name = request.POST['From']
    sender_number = request.POST['ProfileName']
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama3-8b-8192",
    )
    print(chat_completion.choices[0].message.content)
    gpt_response = chat_completion.choices[0].message.content
    twilio_client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"{gpt_response}",
    to='whatsapp:+56963911679'
    )
    response = MessagingResponse()
    return HttpResponse(str(response))

