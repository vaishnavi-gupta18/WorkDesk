from django.shortcuts import render,redirect
from django.http.response import Http404
from django.http import HttpResponse 
from django.contrib.auth.models import Group
import requests
from django.contrib.auth import login,authenticate
from decouple import config

from .models import User


class UserBackend:
    def authenticate(self,request,user_name):
        if user_name:
            try:
                user = User.objects.get(username=user_name)
                return user
            except User.DoesNotExist:
                User.objects.create(username=user_name)
                group = Group.objects.get(name='normaluser')
                User.groups.add(group)
        return None
    
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def Login(request):  
    return redirect('{}client_id={}&redirect_uri={}'.format(config("SITE"),config("CLIENT_ID"),config("REDIRECT_URI")))

def AfterLogin(request):
    response = request.GET
    try:
        code = response["code"]
        post_data = {'client_id':'{}'.format(config("CLIENT_ID")),
        "client_secret":"{}".format(config("CLIENT_SECRET")),
        "grant_type":"authorization_code",
        "redirect_uri":"{}".format(config("REDIRECT_URI")),
        "code":"{}".format(code)
        }

        token_request = requests.post('{}'.format(config("CODE_SITE")), data=post_data)
        if token_request.status_code == 200:
            response = token_request.json()
        else:
            if token_request.status_code == 404:
                raise Http404("Page not found")
            else:
                return HttpResponse(status=token_request.status_code) 

        access_token=response["access_token"]
        data_request=requests.get('{}'.format(config("TOKEN_SITE")), headers={"Authorization":"Bearer {}".format(access_token)})
        if data_request.status_code == 200:
            data = data_request.json()
        else:
           return HttpResponse(status=token_request.status_code) 
        
        roles=data["person"]["roles"]
        roles_check=False
        for i in range(len(roles)):
            if roles[i]["role"] == 'Maintainer':
                roles_check=True
        if roles_check:
            user = authenticate(user_name=data["username"])
            user.save()
            login(request,user)
        else:
            return redirect('/workdesk')
    except:
        raise Http404("Page not found")
    return render(request, 'workdesk/login.html')


