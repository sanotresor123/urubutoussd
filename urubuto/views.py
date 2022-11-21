from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt

def urubuto(request):
    if request.method == "POST":
        session_id = request.POST.get("sessionId", None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")
        response = ""
        if text == '':
            response = "CON Pay school fees with UrubutoPay \n"
            response += "1. Dial your code to enter \n"
            response += "2. Choose 2 \n"
        elif text == '1':
            response = "CON welcome to Urubuto \n"
        elif text == '1*1':
             response = "CON Pay school fees with UrubutoPay \n"
             response += "1. Choose Language \n"
             response += "2. Welcome to UrubutoPay \n"
             response += "3. Enter Merchant code : \n"
        elif text == '1*2':
             response = "CON Welcome to UrubutoPay \n"
             response += "1. Enter student reg number \n"
             response += "2. Enter your school name \n"
             response += "3. Enter payer names \n"
             response += "See your payment"
             return HttpResponse(response)
        return HttpResponse(response)                 
