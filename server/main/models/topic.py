__all__ = ['Topic']
from django.db import models

# Create your models here.
class Topic(models.Model):
  class Meta():  # Meta 可用于定义数据表名，排序方式等。
    verbose_name="topics" #指明一个易于理解和表示的单词形式的对象。
    db_table = "topics" #声明数据表的名。
  
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  desc = models.TextField()

  def __str__(self):
    return self.username

  def get_obj(self):
    return {
      'id': self.id,
      'name': self.name,
      'desc': self.desc
    }