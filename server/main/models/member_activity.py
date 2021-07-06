__all__ = ['MemberActivity']
from django.db import models

# Create your models here.
class MemberActivity(models.Model):
    class Meta():  # Meta 可用于定义数据表名，排序方式等。
        verbose_name="member_activity" #指明一个易于理解和表示的单词形式的对象。
        db_table = "member_activity" #声明数据表的名。
    
    member_id = models.IntegerField()
    activity_id = models.IntegerField()
    join_time = models.CharField(max_length=20)

    def __str__(self):
        return '%s%s'%(self.member_id, self.activity_id)