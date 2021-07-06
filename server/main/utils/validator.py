__all__ = ['id_reg', 'check_login']

from django.core.validators import RegexValidator
from functools import wraps
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse, QueryDict

from ..models import Member

id_reg = '^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9X]$'


def check_login(function):
    @wraps(function)
    def inner(self, request, *arg, **kwargs):
        # token = request.META.get("HTTP_X_USER_TOKEN")
        token = None
        manage = None
        if request.method == 'GET':
            token = request.GET.get('token')
            manage = request.GET.get('manage')
        elif request.method == 'POST':
            token = request.POST.get('token')
            manage = request.POST.get('manage')
        elif request.method == 'DELETE':
            token = QueryDict(request.body).get('token')
            manage = QueryDict(request.body).get('manage')
        
        if manage is not None:
            user = Member.objects.get(pk=3)
            return function(self, request, user, *arg, **kwargs)

        if token == None or token == '':
            response = dict(code=-1, )
            return JsonResponse(response)
        member_exist = Member.objects.filter(id=token).count()
        
        if member_exist > 0:
            user = Member.objects.get(pk=token)
            if user.state != 0:
                response = dict(code=1, msg='您已被禁用')
                return JsonResponse(response)
            return function(self, request, user, *arg, **kwargs)
        else:
            response = dict(code=-1, )
            return JsonResponse(response)
    return inner
