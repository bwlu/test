from django import forms
from django.views import View
from django.db.models import Max,Min,Q
from ..utils import (
    correct_response, err_response_with_desc,generate_list_dict,check_login
)
from ..models import User
from ..models import Member
import json
from hashlib import md5

class Login(View):
	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		password = md5(password.encode('utf8')).hexdigest()
		member = Member.objects.filter(name=username, password=password)
		arr_list = ['id', 'name', 'nickname', 'birth']
		if member.count() > 0:
			response = generate_list_dict(arr_list,member)[0]
			return correct_response({'token': response['id'], 'name': response['name'], 'nickname': response['nickname'], 'birth': response['birth']})
		else:
			return err_response_with_desc('用户名或密码错误')

class ManageLogin(View):
	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		password = md5(password.encode('utf8')).hexdigest()
		user = User.objects.filter(username=username, password=password)
		arr_list = ['username']
		if user.count() > 0:
			response = generate_list_dict(arr_list,user)[0]
			return correct_response({'token': response['username']})
		else:
			return err_response_with_desc('用户名或密码错误')
