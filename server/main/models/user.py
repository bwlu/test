__all__ = ['User']
from django.db import models

# Create your models here.
class User(models.Model):
    class Meta():  # Meta 可用于定义数据表名，排序方式等。
        verbose_name="users" #指明一个易于理解和表示的单词形式的对象。
        db_table = "users" #声明数据表的名。
    
    username = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username