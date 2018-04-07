from django.shortcuts import render
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .config import username, apikey
from django.views.decorators.csrf import csrf_exempt
from .models import User, session_levels
import datetime
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def ussd_callback(request):
    '''
    function to handle callback calls from africa's talking api
    '''
    if request.method == 'POST' and request.POST:
        sessionId = request.POST.get('sessionId')
        serviceCode = request.POST.get('serviceCode')
        phoneNumber = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        now = datetime.datetime.now()


        textList = text.split('*')
        userResponse = textList[-1].strip()

        level = len(textList)-1

        try:
            user, create = User.objects.get_or_create(phonenumber=phoneNumber)
        except User.DoesNotExist as e:
            level = 0

        if level == 0:
            if userResponse == "":
                response = "CON Welcome to hudumia mama. Are you an expectant mother or a midwife?\n"
                response += "1. I am an expectant mother\n"
                response += "2. I am a midwife\n"

                return HttpResponse(response, content_type='text/plain')

            session_level1 = User.objects.get(phonenumber=phoneNumber)
            session_level1.level = 1
            session_level1.type_of_user = userResponse
            session_level1.save()
            response = "CON Please enter your name:\n"

            return HttpResponse(response, content_type='text/plain')

        if level == 1:
            session_level2 = User.objects.get(phonenumber=phoneNumber)
            session_level2.level = 2
            session_level2.name = userResponse
            session_level2.save()
            response = "CON Fill in your National id number?"
            return HttpResponse(response, content_type='text/plain')

        if level == 2:
            session_level3 = User.objects.get(phonenumber=phoneNumber)
            session_level3.level = 3
            session_level3.national_id = userResponse
            session_level3.save()
            response = "CON Fill in your county? e.g.\n  Nairobi\n Uasin Gishu\n Machakos\ne.t.c ..."

            return HttpResponse(response, content_type='text/plain')

        if level == 3:
            session_level4 = User.objects.get(phonenumber=phoneNumber)
            session_level4.level = 4
            session_level4.location = userResponse
            session_level4.save()
            response = "CON What is your closest town or market center?.\n e.g. Makutano"

            return HttpResponse(response, content_type='text/plain')

        if level == 4:
            session_level4 = User.objects.get(phonenumber=phoneNumber)
            session_level4.level = 5
            session_level4.nearest_town = userResponse
            session_level4.save()
            response = "END Your request has been received. \n We will send you a message with contact details of a midwife/mother that matches your request."
            return HttpResponse(response, content_type='text/plain')