from django.db import models

# Create your models here.

class Users(models.Model):  #继承models类
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    size = models.IntegerField(default=2)
    text1 = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def update_users(self, name=None, phone=None, size=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if size:
            self.size = size
        self.save()  # 保存修改到数据库
        return self  # 可选：返回自身用于链式调用

## 要查哪个表就复制写上，注意这里默认的表名带appsdemo_表名
class Migrations(models.Model):  #继承models类
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name