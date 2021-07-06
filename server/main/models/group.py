__all__ = ['Group']

from django.db import models
from datetime import datetime
import json

# 群体表
class Group(models.Model):

	class Meta():  # Meta 可用于定义数据表名，排序方式等。
	    verbose_name="groups" #指明一个易于理解和表示的单词形式的对象。
	    db_table = "groups" #声明数据表的名。

	id = models.AutoField(primary_key=True,verbose_name=u"")
	name = models.CharField(max_length=100,verbose_name=u"")
	desc = models.TextField(verbose_name=u"")
	photo = models.CharField(max_length=255,verbose_name=u"")
	members = models.IntegerField(verbose_name=u"")
	create_time = models.CharField(max_length=100,verbose_name=u"")
	who = models.IntegerField(verbose_name=u"")
	rating = models.CharField(max_length=100,verbose_name=u"")
	location = models.CharField(max_length=100,verbose_name=u"")
	main_topic = models.CharField(max_length=255,verbose_name=u"")
	topics = models.CharField(max_length=255,verbose_name=u"")
	verify = models.IntegerField(verbose_name=u"")
	state = models.IntegerField(verbose_name=u"")

	def __str__(self):
		info = {
			'id': self.id,
			'name': self.name,
			'desc': self.desc,
			'photo': self.photo,
			'members': self.members,
			'create_time': self.create_time,
			'who': self.who,
			'rating': self.rating,
			'location': self.location,
			'main_topic': self.main_topic,
			'topics': self.topics,
			'verify': self.verify,
			'state': self.state
		}
		return json.dumps(info)

	def get_obj(self):
		return {
			'id': self.id,
			'name': self.name,
			'desc': self.desc,
			'photo': self.photo,
			'members': self.members,
			'create_time': self.create_time,
			'who': self.who,
			'rating': self.rating,
			'location': self.location,
			'main_topic': self.main_topic,
			'topics': self.topics,
			'verify': self.verify,
			'state': self.state
		}