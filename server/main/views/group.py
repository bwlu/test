from django import forms
from django.views import View
from django.db.models import Max,Min,Q
from django.http import JsonResponse, QueryDict
from ..utils import (
    correct_response, err_response_with_desc,generate_list_dict,check_login, generate_value_list_dict
)
from ..models import Group, GroupMember, Member, Activity
import json, time

class GroupList(View):
	@check_login
	def get(self,request,user):
		page = int(request.GET.get('page'))
		name = request.GET.get('name')
		state = request.GET.get('state')
		search = {}
		if name is not None and name is not '':
			search['name__contains'] = name
		if state is not None and state is not '':
			search['state'] = int(state)
		arr_list = [
			'id',
			'name',
			'members',
			'create_time',
			'location',
			'main_topic',
			'who',
			'state',
		]
		start = (page - 1) * 20
		end = page * 20
		groups = Group.objects.filter(**search)[start:end]
		all_count = Group.objects.filter(**search).count()
		response = generate_list_dict(arr_list,groups)
		return correct_response({'all_count': all_count, 'list':response})
class GroupDetail(View):
	@check_login
	def get(self,request,user):
		mid = user.id
		id = request.GET.get('id')
		group = Group.objects.get(pk=id)
		group_obj = group.get_obj()
		gm = GroupMember.objects.filter(group_id=id, verify=1).values("member_id")
		gmjt = GroupMember.objects.filter(group_id=id, verify=1).values("join_time")
		members = []
		memberids = []
		if len(gm) != 0:
			memberids = generate_value_list_dict('member_id', gm)['member_id']
			memberjts = generate_value_list_dict('join_time', gmjt)['join_time']
			members_qs = Member.objects.filter(id__in=memberids, state=0)
			members = generate_list_dict([
				'id', 'name','state',
			],members_qs)
			for i in range(0, len(members)):
				members[i]['join_time'] = memberjts[i]
		activity_qs = Activity.objects.filter(group_id=id, verify=1, state=1)
		activitys = generate_list_dict([
			'id', 'title', 'desc', 'location', 'main_topic', 'create_time', 'status'
		],activity_qs)
		gmvr = GroupMember.objects.filter(group_id=id,member_id=mid, verify=0, rating='group').count()
		return correct_response({
			'info': group_obj,
			'members': members,
			'activitys': activitys,
			'is_member': user.id in memberids,
			'is_invite': gmvr > 0
		})
	@check_login
	def post(self,request,user):
		req = request.POST
		current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			group = Group()
			group.name = req.get('name')
			group.desc = req.get('desc')
			group.location = req.get('location')
			group.photo = req.get('photo')
			group.main_topic = req.get('main_topic')
			group.topics = req.get('topics')
			group.create_time = current_time
			group.members = 1
			group.who = user.id
			group.state = 1
			group.save()
			gm = GroupMember()
			gm.group_id = group.id
			gm.member_id = user.id
			gm.join_time = current_time
			gm.verify = 1
			gm.save()
		except Exception as e:
			print(e)
			return err_response_with_desc('好像哪里出错了')
		return correct_response({'data': '恭喜您，创建成功，快去邀请小伙伴吧'})
	@check_login
	def delete(self,request,user):
		id = QueryDict(request.body).get('id')
		try:
			Group.objects.filter(id=id).update(state=0)
		except:
			return err_response_with_desc('好像哪里出错了')
		return correct_response({"data": '已删除'})

class GroupMembers(View):
	@check_login
	def get(self,request,user):
		id = request.GET.get('id')
		try:
			gm = GroupMember.objects.filter(group_id=id)
			response = generate_list_dict(['member_id','verify'],gm)
		except:
			return err_response_with_desc('操作失败')
		return correct_response({"list": response})
	@check_login
	def post(self,request,user):
		id = request.POST.get('id')
		mid = request.POST.get('mid')
		current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			gm = GroupMember()
			gm.group_id = id
			gm.member_id = mid
			gm.join_time = current_time
			gm.verify = 0
			gm.rating = 'group'
			gm.save()
		except Exception as e:
			print(e)
			return err_response_with_desc('无法邀请')
		return correct_response()
	@check_login
	def delete(self,request,user):
		id = QueryDict(request.body).get('id')
		mid = QueryDict(request.body).get('mid')
		try:
			gm = GroupMember.objects.filter(group_id=id, member_id=mid)
			gm.delete()
		except:
			return err_response_with_desc('移除失败')
		return correct_response({"data": '移除成功'})

class GroupActivitys(View):
	@check_login
	def delete(self,request,user):
		id = QueryDict(request.body).get('id')
		aid = QueryDict(request.body).get('aid')
		try:
			ga = Activity.objects.filter(group_id=id, id=aid).update(state=0)
		except:
			return err_response_with_desc('删除失败')
		return correct_response({"data": '删除成功'})

class GroupApply(View):
	@check_login
	def get(self,request,user):
		id = request.GET.get('id')
		name = request.GET.get('name')
		search = {}
		if name is not None and name is not '':
			search['name__contains'] = name
		gm = GroupMember.objects.filter(group_id=id, verify=0, rating='member').values('member_id')
		gmjt = GroupMember.objects.filter(group_id=id, verify=0, rating='member').values('join_time')
		if gm.count() == 0:
			return correct_response({'list': []})
		memberids = generate_value_list_dict('member_id', gm)['member_id']
		memberjts = generate_value_list_dict('join_time', gmjt)['join_time']
		arr_list = [
			'id',
			'name',
			'nickname',
			'bio'
		]
		members = Member.objects.filter(id__in=memberids).filter(**search)
		response = generate_list_dict(arr_list,members)
		for i in range(0, len(response)):
			response[i]['join_time'] =  memberjts[i]
		return correct_response({'list': response})

	@check_login
	def post(self,request,user):
		gid = request.POST.get('id')
		mid = request.POST.get('mid')
		try:
			gm = GroupMember.objects.filter(group_id=gid, member_id=mid).update(verify=1)
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '已同意'})

	@check_login
	def delete(self,request,user):
		gid = QueryDict(request.body).get('id')
		mid = QueryDict(request.body).get('mid')
		try:
			gm = GroupMember.objects.filter(group_id=gid, member_id=mid)
			gm.delete()
		except:
			return err_response_with_desc('操作失败，请稍后再试')
		return correct_response({"data": '已拒绝'})
	# @check_login
	# def post(self,request):
	# 	group_id = request.POST.get('group_id')
	# 	try:
	# 		group = Group.objects.get(pk=group_id)
	# 		group.name = group_name
	# 		group.save()
	# 	except Exception as e:
	# 		return correct_response(str(e))
	# 	return correct_response({})

# class GroupAdd(View):
# 	@check_login
# 	def post(self,request):
# 		group_name = request.POST.get('group_name')
# 		try:
# 			group = Group()
# 			group.name = group_name
# 			group.user_id = username
# 			group.save()
# 		except Exception as e:
# 			return correct_response(str(e))
# 		return correct_response({})

# class GroupDelete(View):
# 	@check_login
# 	def post(self,request):
# 		group_id = request.POST.get('group_id')
# 		try:
# 			group = Group.objects.get(pk=group_id)
# 			group.delete()
# 		except Exception as e:
# 			return correct_response(str(e))
# 		return correct_response({})
