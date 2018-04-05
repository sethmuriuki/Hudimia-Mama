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