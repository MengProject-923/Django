from django.db import models

# 用户
class Users(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    sex = models.IntegerField()
    notes =  models.TextField()

    def __str__(self):
        return self.name

# 服务主机明细
class Serverhosts(models.Model):
    serverhost_id = models.IntegerField()
    hostname = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    images = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

# 固定资产明细
class Fixedassets(models.Model):
    fixed_asset_id = models.IntegerField()
    name = models.CharField(max_length=50)          # 物品名称
    user = models.CharField(max_length=50)          # 使用人
    department = models.CharField(max_length=50)    # 使用部门
    number = models.IntegerField()                  # 数量
    collectiontime = models.DateTimeField()         # 领用时间
    isuse = models.IntegerField()                   # 是否领用
    notes = models.TextField()                      # 备注

    def __str__(self):
        return self.name
