from django.shortcuts import render
from django.http import JsonResponse
from backend.models import *
from backend.utils import *


def home(request):
    return JsonResponse({"success": False})

def login(request):
	output = {'success':False}
	if request.method == 'GET':
		email = request.GET.get('email','') #request.POST['email']
		password = request.GET.get('password','')
		try:
			user = Access.objects.get(user_email=email, password=password)
			output['success'] = True
			output['msg'] = 'Logged in'
		except:
			output['msg'] = 'Invalid username or password'
			
	return JsonResponse(output)


def register(request):
	output = {'success':False}
	if request.method == 'GET':
		email = request.GET.get('email','') #request.POST['email']
		password = request.GET.get('password','')
		try:
			user = Access.objects.get(user_email=email, password=password)
			output['msg'] = 'The user is already registered.'
		except Access.DoesNotExist:
			user = Access.objects.create(user_email=email, password=password,creation_date= getTodayDate(), authorised=1)
			user.save()
			output['msg'] = 'Account Created'
			output['success'] = True

		except Exception as ex:
			output['msg'] = 'Cannot create user at the moment. %s'%str(ex)
			
	return JsonResponse(output)	