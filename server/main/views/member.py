from django import forms
from django.views import View
from django.db.models import Max,Min,Q
from django.http import JsonResponse, QueryDict
from ..utils import (
    correct_response, err_response_with_desc,generate_list_dict,check_login,generate_value_list_dict
)
from ..models import Member, Activity, Group, GroupMember
import json, time

class MemberDetail(View):
	@check_login
	def post(self,request,user):
		mid = user.id
		req = request.POST
		try:
			member = Member.objects.get(pk=mid)
			member.name = req.get('name')
			member.nickname = req.get('nickname')
			member.birth = req.get('birth')
			member.save()
		except:
			return err_response_with_desc('好像哪里出错了')
		return correct_response({"data": '保存成功'})
class MemberHome(View):
	@check_login
	def get(self,request,user):
		count = int(request.GET.get('count'))
		arr_list = [
			'id',
			'title',
			'desc',
			'location',
			'main_topic',
			'images'
		]
		item_list = Activity.objects.filter(state=1)
		all_count = Activity.objects.filter(state=1).count()
		response = generate_list_dict(arr_list,item_list)[:count]
		return correct_response({'all_count':all_count,'list':response})

class MemberLike(View):
	@check_login
	def get(self,request,user):
		count = int(request.GET.get('count'))
		arr_list = [
			'id',
			'title',
			'desc',
			'location',
			'main_topic',
			'images'
		]
		item_list = Activity.objects.filter(state=1)
		all_count = Activity.objects.filter(state=1).count()
		response = generate_list_dict(arr_list,item_list)[:count]
		return correct_response({'all_count':all_count,'list':response})

class MemberHot(View):
	@check_login
	def get(self,request,user):
		count = int(request.GET.get('count'))
		arr_list = [
			'id',
			'title',
			'location',
			'create_time',
			'main_topic',
			'images'
		]
		item_list = Activity.objects.filter(state=1, id__gt=244526405)
		all_count = Activity.objects.filter(state=1).count()
		response = generate_list_dict(arr_list,item_list)[:count]
		return correct_response({'all_count':all_count,'list':response})

class MemberHotGroup(View):
	@check_login
	def get(self,request,user):
		count = int(request.GET.get('count'))
		arr_list = [
			'id',
			'name',
			'desc',
			'photo',
			'members',
			'create_time',
			'location',
			'main_topic'
		]
		item_list = Group.objects.filter(state=1)
		all_count = Group.objects.filter(state=1).count()
		response = generate_list_dict(arr_list,item_list)[:count]
		return correct_response({'all_count':all_count,'list':response})

class MemberGroup(View):
	@check_login
	def get(self,request,user):
		mid = user.id
		groups = GroupMember.objects.filter(member_id=mid).values("group_id")
		gids = generate_value_list_dict('group_id', groups)['group_id']
		arr_list = [
			'id',
			'name',
			'desc',
			'photo',
			'members',
			'create_time',
			'location',
			'main_topic'
		]
		item_list = Group.objects.filter(id__in=gids,state=1)
		item_who = Group.objects.filter(who=mid,state=1).values('id')
		cids = []
		if len(item_who) != 0:
			cids = generate_value_list_dict('id', item_who)['id']
		response = generate_list_dict(arr_list,item_list)
		for item in response:
			item['who'] = item['id'] in cids
		return correct_response({'list':response})

class MemberList(View):
	@check_login
	def get(self,request,user):
		page = int(request.GET.get('page'))
		name = request.GET.get('name')
		state = request.GET.get('state')
		manage = request.GET.get('manage')
		search = {}
		if manage is None or manage is '':
			search['state'] = 0
		if name is not None and name is not '':
			search['name__contains'] = name
		if state is not None and state is not '':
			search['state'] = int(state)
		
		arr_list = [
			'id',
			'name',
			'nickname',
			'state',
			'bio'
		]
		start = (page - 1) * 20
		end = page * 20
		members = Member.objects.filter(**search)[start:end]
		all_count = Member.objects.filter(**search).count()
		response = generate_list_dict(arr_list,members)
		return correct_response({'all_count': all_count, 'list':response})

class MemberInvite(View):
	@check_login
	def get(self,request,user):
		mid = user.id
		gm = GroupMember.objects.filter(member_id=mid, verify=0).values('group_id')
		if len(gm) == 0:
			return correct_response({'list':[]})
		groupids = generate_value_list_dict('group_id', gm)['group_id']
		print(groupids)
		arr_list = [
			'id',
			'name',
			'desc',
			'photo',
			'members',
			'create_time',
			'location',
			'main_topic'
		]
		groups = Group.objects.filter(id__in=groupids, state=1)
		response = generate_list_dict(arr_list,groups)
		return correct_response({'list':response})

class MemberGroupJoinExit(View):
	@check_login
	def post(self,request,user):
		mid = user.id
		gid = request.POST.get('id')
		current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			gm = GroupMember()
			gm.group_id = gid
			gm.member_id = mid
			gm.join_time = current_time
			gm.verify = 0
			gm.rating = 'member'
			gm.save()
		except:
			return err_response_with_desc('无法加入，好像哪里出错了')
		return correct_response({"data": '申请成功'})

	@check_login
	def delete(self,request,user):
		mid = user.id
		gid = QueryDict(request.body).get('id')
		try:
			gm = GroupMember.objects.filter(group_id=gid, member_id=mid)
			gm.delete()
		except:
			return err_response_with_desc('退出失败，请稍后再试')
		return correct_response({"data": '已退出'})

class MemberGroupAgreeRefuse(View):
	@check_login
	def post(self,request,user):
		mid = user.id
		gid = request.POST.get('id')
		try:
			GroupMember.objects.filter(group_id=gid, member_id=mid).update(verify=1)
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '加入成功'})

	@check_login
	def delete(self,request,user):
		mid = user.id
		gid = QueryDict(request.body).get('id')
		try:
			gm = GroupMember.objects.filter(group_id=gid, member_id=mid)
			gm.delete()
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '已拒绝'})

class MemberEnable(View):
	@check_login
	def post(self,request,user):
		mid = request.POST.get('id')
		try:
			Member.objects.filter(id=mid).update(state=0)
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '启用成功'})

	@check_login
	def delete(self,request,user):
		mid = QueryDict(request.body).get('id')
		try:
			Member.objects.filter(id=mid).update(state=1)
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '禁用成功'})