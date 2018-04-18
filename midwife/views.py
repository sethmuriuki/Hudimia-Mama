from django.shortcuts import render
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .config import username, apikey
from django.views.decorators.csrf import csrf_exempt
from .models import User, session_levels
import datetime
from django.http import HttpResponse
from .methods import get_users, get_phonenumbers,details_generator, final_list

# Create your views here.
username = username
apiKey = apikey

@csrf_exempt
def ussd_callback(request):
    '''
    function to handle callback calls from africa's talking api
    '''
    if request.method == 'POST' and request.POST:
        sessionId = request.POST.get('sessionId')
        serviceCode = request.POST.get('serviceCode')
        phoneNumber= request.POST.get('phoneNumber')
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
            users = User.objects.create(type_of_user=textList[0],name=textList[1])
            users.save()
            response = "END Your request has been received. \n We will send you a message with contact details of a midwife/mother that matches your request."
            current_location = textList[3]
            current_phonenumber = phoneNumber
            current_user= textList[0]
            current_name = textList[2]
            current_idno=textList[3]

            requested_users = User.requested_users(current_user)
            my_users = get_users(requested_users, current_location, textList[4])
            print(my_users)
            # # # list_location= requested_location(current_location)
            # # # list_name= requested_name(current_name)
            # # # results_list = final_list(requested_users,list_location,list_name)
            # # found_phonenumbers = get_phonenumbers(results_list)
            #
            # contacts= details_generator(found_phonenumbers)
            # print(contacts)


            to = phoneNumber
            message = 'Thank you ' + user.name + ' for using our services.\n' \
                                                 'This is your entry:\n\n' \
                                                 'Name: ' + textList[1] + '\n' \
                                                 'Location: ' + textList[3] + '\n' \
                                                 'Nearest town: ' + \
                      textList[4] + '\n\n' \
                                    'If this entry is accurate, we will send you information matching your request.\n' \
                                    'If you would like to make another entry dial. \n*384*5611#'
            # message1 = 'Find below contact the numbers below matching your request: \n' + contacts

            gateway = AfricasTalkingGateway(username, apiKey)

            try:
                # That's it, hit send and we'll take care of the rest.

                results = gateway.sendMessage(to, message)
                # results1 = gateway.sendMessage(to, message1)

                for recipient in results:
                    # status is either "Success" or "error message"
                    print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                        recipient['status'],
                                                                        recipient['messageId'],
                                                                        recipient['cost']))

                # for recipient in results1:
                #     # status is either "Success" or "error message"
                #     print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                #                                                         recipient['status'],
                #                                                         recipient['messageId'],
                #                                                         recipient['cost']))

            except AfricasTalkingGatewayException as e:
                print('Encountered an error while sending: %s' % str(e))

            return HttpResponse(response, content_type='text/plain')