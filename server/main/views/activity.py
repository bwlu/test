from django import forms
from django.views import View
from django.db.models import Max,Min,Q
from django.http import JsonResponse, QueryDict
from ..utils import (
    correct_response, err_response_with_desc,generate_list_dict,check_login, get_list_key_value
)
from ..models import Activity, MemberActivity
import json, time

class ActivityList(View):
	@check_login
	def get(self,request,user):
		page = int(request.GET.get('page'))
		name = request.GET.get('name')
		state = request.GET.get('state')
		search = {}
		if name is not None and name is not '':
			search['title__contains'] = name
		if state is not None and state is not '':
			search['state'] = int(state)
		arr_list = [
			'id',
			'title',
			'desc',
			'status',
			'location',
			'main_topic',
			'create_time',
			'group_id',
			'state',
		]
		start = (page - 1) * 20
		end = page * 20
		item_list = Activity.objects.filter(**search)[start:end]
		all_count = Activity.objects.filter(**search).count()
		response = generate_list_dict(arr_list,item_list)
		return correct_response({'all_count':all_count,'list':response})

class ActivityDetail(View):
	@check_login
	def get(self,request,user):
		id = request.GET.get('id')
		item = Activity.objects.get(pk=id)
		response = item.get_obj()
		response['phone'] = '18232386357'
		return correct_response(response)
	@check_login
	def post(self,request,user):
		req = request.POST
		current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			activity = Activity()
			activity.title = req.get('title')
			activity.desc = req.get('desc')
			activity.location = req.get('location')
			activity.images = req.get('images')
			activity.main_topic = req.get('main_topic')
			activity.topics = req.get('topics')
			activity.status = req.get('status')
			activity.group_id = req.get('group_id')
			activity.create_time = current_time
			activity.verify = 1
			activity.state = 1
			activity.save()
		except Exception as e:
			print(e)
			return err_response_with_desc('好像哪里出错了')
		return correct_response({'data': '恭喜您，创建成功'})
	@check_login
	def delete(self,request,user):
		id = QueryDict(request.body).get('id')
		try:
			Activity.objects.filter(id=id).update(state=0)
		except:
			return err_response_with_desc('好像哪里出错了')
		return correct_response({"data": '已删除'})

class ActivityJoin(View):
	@check_login
	def post(self,request,user):
		aid = request.POST.get('id')
		uid = user.id
		current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			member_activity = MemberActivity()
			member_activity.activity_id = aid
			member_activity.member_id = uid
			member_activity.join_time = current_time
			member_activity.verify = 1
			member_activity.save()
		except Exception as e:
			print(e)
			return err_response_with_desc('无法报名')
		return correct_response()
