__all__ = ['Member']

from django.db import models
from datetime import datetime
import json

# 群体表
class Member(models.Model):

	class Meta():  # Meta 可用于定义数据表名，排序方式等。
	    verbose_name="member" #指明一个易于理解和表示的单词形式的对象。
	    db_table = "member" #声明数据表的名。

	id = models.AutoField(primary_key=True,verbose_name=u"")
	name = models.CharField(max_length=100,verbose_name=u"")
	nickname = models.CharField(max_length=100,verbose_name=u"")
	bio = models.TextField(verbose_name=u"")
	birth = models.CharField(max_length=20,verbose_name=u"")
	password = models.CharField(max_length=100,verbose_name=u"")
	preference = models.IntegerField(verbose_name=u"")
	main_topic = models.CharField(max_length=255,verbose_name=u"")
	topics = models.CharField(max_length=255,verbose_name=u"")
	state = models.IntegerField(verbose_name=u"")

	def __str__(self):
		info = {
			'id': self.id,
			'name': self.name,
			'nickname': self.nickname,
			'bio': self.bio,
			'birth': self.birth,
			'password': self.password,
			'preference': self.preference,
			'main_topic': self.main_topic,
			'topics': self.topics,
			'state': self.state,
		}
		return json.dumps(info)

	def get_obj(self):
		return {
			'id': self.id,
			'name': self.name,
			'nickname': self.nickname,
			'bio': self.bio,
			'birth': self.birth,
			'password': self.password,
			'preference': self.preference,
			'main_topic': self.main_topic,
			'topics': self.topics,
			'state': self.state,
		}