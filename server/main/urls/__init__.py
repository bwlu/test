from django.conf.urls import include,url
from ..views import Login, ManageLogin, ImageUpload
from ..views import GroupList, GroupDetail, GroupMembers, GroupActivitys, GroupApply
from ..views import ActivityList, ActivityDetail, ActivityJoin
from ..views import (
    MemberHome, MemberLike, MemberHot, MemberHotGroup, MemberGroup, MemberList, MemberInvite,
    MemberGroupJoinExit, MemberGroupAgreeRefuse, MemberDetail
)
from ..views import (
    MemberEnable
)

urlpatterns = [
    url(r'^login/$',Login.as_view()),
    url(r'^manage/login/$',ManageLogin.as_view()),
    url(r'^image/upload/$',ImageUpload.as_view()),
    url(r'^activity/list/$',ActivityList.as_view()),
    url(r'^member/$',MemberDetail.as_view()),
    url(r'^member/home/$',MemberHome.as_view()),
    url(r'^member/like/$',MemberLike.as_view()),
    url(r'^member/hot/$',MemberHot.as_view()),
    url(r'^member/hot-group/$',MemberHotGroup.as_view()),
    url(r'^member/group/$',MemberGroup.as_view()),
    url(r'^member/list/$',MemberList.as_view()),
    url(r'^member/invite/$',MemberInvite.as_view()),
    url(r'^member/join/$',MemberGroupJoinExit.as_view()),
    url(r'^member/agree/$',MemberGroupAgreeRefuse.as_view()),
    url(r'^group/$',GroupDetail.as_view()),
    url(r'^group/members/$',GroupMembers.as_view()),
    url(r'^group/activitys/$',GroupActivitys.as_view()),
    url(r'^group/apply/$',GroupApply.as_view()),
    url(r'^activity/$',ActivityDetail.as_view()),
    url(r'^activity/join/$',ActivityJoin.as_view()),
    # 管理端
    url(r'^member/enable/$',MemberEnable.as_view()),
    url(r'^group/list/$',GroupList.as_view()),
]
