from django.shortcuts import render
from django.http import JsonResponse
from backend.models import Access,ResetPwd
from backend.utils import *

def home(request):
    return JsonResponse({"success": False})

def login(request):
	output = {'success':False}
	if request.method == 'GET':
		email = request.GET.get('email') #request.POST['email']
		password = request.GET.get('password')
		try:
			user = Access.objects.filter(user_email=email,password=password)
			if user.count():
				output['success'] = True
				output['msg'] = 'Logged in'
		except:
			output['msg'] = 'Invalid username or  password'

	return JsonResponse(output)

def register(request):
	output = {'success':False}
	if request.method == 'GET':
		email = request.GET.get('email')
		password = request.GET.get('password')
		try:
			user = Access.objects.filter(user_email=email)
			if user.count():
				output['msg'] = 'The user is already registered.'
			else:
				user = Access.objects.create(user_email=email, password=password,creation_date= getTodayDate(), authorised=1)
				user.save()
				output['msg'] = 'Account Created Successfully'
				output['success'] = True
		except Exception as ex:
			output['msg'] = 'Cannot create user at the moment. %s'%str(ex)
	return JsonResponse(output)

def reset_password(request):#in progress
	output = {'success':False}
	if request.method == 'GET':
		email = request.GET.get('email')
		reset_code = request.GET.get('code')
		old_password = request.GET.get('old_password')
		new_password = request.GET.get('new_password')
		try:
			user = ResetPwd.objects.filter(emailid=email,code=reset_code)
			if user.count():
				output['success'] = True
				output['msg'] = 'Logged in'
		except:
			output['msg'] = 'Invalid username or  password'

	return JsonResponse(output)
