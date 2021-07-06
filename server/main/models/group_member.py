__all__ = ['GroupMember']
from django.db import models

# Create your models here.
class GroupMember(models.Model):
    class Meta():  # Meta 可用于定义数据表名，排序方式等。
        verbose_name="group_member" #指明一个易于理解和表示的单词形式的对象。
        db_table = "group_member" #声明数据表的名。
        # unique_together=("member_id","group_id")
        unique_together=(("member_id","group_id"),)
    
    member_id = models.IntegerField()
    group_id = models.IntegerField()
    join_time = models.CharField(max_length=20)
    verify = models.IntegerField()
    rating = models.CharField(max_length=20)

    def __str__(self):
        return '%s,%s'%(self.member_id, self.group_id)