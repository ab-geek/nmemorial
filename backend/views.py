from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse



from backend.models import Access,ResetPwd,Memorial
from backend.utils import *

def home(request):
    return JsonResponse({"success": False})

#http://127.0.0.1:8000/api/login/?user_email=test@gmail.com&password=new
def login(request):#accepts empty parameters too
	output = {'success':False}
	if request.method == 'GET':
		param_dict = request.GET
		try:
			user = Access.objects.filter(user_email=param_dict['user_email'],password=param_dict['password'])
			if user.count():
				output['success'] = True
			else:
				output['msg']='invalid credentials'
		except:
			output['success']=False
	return JsonResponse(output)


#http://127.0.0.1:8000/api/register/?username=chris@locmyd.onlneagain&password=maley014
def register(request):#validations and email verification ..etc..not applicable yet
	output = {'success':False}
	if request.method == 'GET':
		param_dict = request.GET
		try:
			user = Access.objects.filter(user_email=param_dict['username'])
			if user.count():
				output['msg'] = 'The user is already registered.'
			else:
				user = Access.objects.create(user_email=param_dict['username'], password=param_dict['password'],creation_date= getTodayDate(), authorised=1)
				user.save()
				output['msg'] = 'Account Created Successfully'
				output['user_id']=user.pk
				output['success'] = True
		except Exception as ex:
			output['msg'] = 'Cannot create user at the moment. %s'%str(ex)
			output['success']=False
	return JsonResponse(output)

#http://127.0.0.1:8000/api/forgot_pw/?user_email=test@gmail.com&old_password=new&new_password=temp&code=kjfdsagd
def forgot_pw(request):#validation like password length,verifying via email not applicable yet
	output = {'success':False}
	if request.method == 'GET':
		param_dict = request.GET
		try:
			check_user = Access.objects.get(user_email=param_dict['user_email'],password=param_dict['old_password'])
			output['validuser']=True
			try:
				change_password = Access.objects.filter(user_email=param_dict['user_email']).update(password=param_dict['new_password'])
				output['success']=True
				output['msg']='Password Changed Successfully'
			except Access.DoesNotExist:
				output['msg']='Unable To change password..please try again'
		except Access.DoesNotExist:
			output['validuser']=False
			output['success']=False
	return JsonResponse(output)

# 127.0.0.1:8000/api/add_story/?accessguid=1&fname=bishnu&mname=prasad&lname=khanal&dob=2016-02-01&dod=2099-02-03&latitude=23.45&longitude=56.45&stry=this is my story . my name is bishnu khanal &relatedlink=www.google.com&profilephoto=bishnu.png

def add_story(request):
	output = {'success':False}
	if request.method == 'GET':
		param_dict = request.GET
		print param_dict
		try:
			add_story = Memorial.objects.create(
												accessguid=param_dict['accessguid'],
												fname=param_dict.get('fname',''),
												mname=param_dict.get('mname',''),
												lname=param_dict.get('lname',''),
												story=param_dict.get('story',''),
												dob=param_dict['dob'],
												dod=param_dict['dod'],
												latitude=param_dict['latitude'],
												longitude=param_dict['longitude'],
												)
			add_story.save()
			output['success']=True
		except Exception as e:
			output['msg']='Unable to add Memorial.Please try again'
			output['exception']=e

	return JsonResponse(output)

# http://127.0.0.1:8000/api/edit_story/51/?accessguid=1&fname=editednae&mname=prasad&lname=khanal&dob=2016-02-10&dod=2099-02-03&latitude=23.45&longitude=56.45&stry=this%20is%20my%20story%20.%20my%20name%20is%20bishnu%20khanal%20&relatedlink=www.google.com&profilephoto=bishnu.png
def edit_story(request,memorial_id):
	output = {'success':False}
	if request.method == 'GET':
		param_dict=request.GET
		try:
			edit_memorial = Memorial.objects.filter(guid=memorial_id).update(
				accessguid=param_dict['accessguid'],
				fname=param_dict.get('fname',''),
				mname=param_dict.get('mname',''),
				lname=param_dict.get('lname',''),
				story=param_dict.get('story',''),
				dob=param_dict['dob'],
				dod=param_dict['dod'],
				latitude=param_dict['latitude'],
				longitude=param_dict['longitude'],
				relatedlink=param_dict.get('relatedlink',''),
				profilephoto=param_dict.get('profilephoto','')
			)
			output['success']=True

		except Memorial.DoesNotExist:
			output['msg']='unable to update'
	return JsonResponse(output)

# http://127.0.0.1:8000/api/delete_story/51/
def delete_story(request,memorial_id):
	output = {'success':False}
	if request.method == 'GET':
		param_dict=request.GET
		try:
			edit_memorial = Memorial.objects.get(guid=memorial_id)
			edit_memorial.delete()
			output['success']=True
		except Memorial.DoesNotExist as e:
			output['msg']=e.message
	return JsonResponse(output)


def search(request,memorial_name):
	output = {'success':False}
	if request.method == 'GET':
		param_dict=request.GET
		search_memorial = Memorial.objects.filter(fname__contains=memorial_name)
		output['results'] = serializers.serialize('json', list(search_memorial), fields=('fname','lname'))
		print output['results']
	return JsonResponse(output)
