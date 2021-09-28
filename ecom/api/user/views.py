from django.contrib.auth.backends import UserModel
from rest_framework import viewsets
from rest_framework.permission import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re

import random

# Create your views here.

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameter only'})
    
    username = request.POST['email']
    password = request.POST['password']

    # validation part

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'password needs to be at least of 3 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email = username)

# matching user's password
        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'previous session exist!'})           
            

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})

        else:
            return JsonResponse({'error': 'Invalid password'})


    except UserModel.DoesNotExist:
        return JsonResponse ({'error': 'Invalid Email'})