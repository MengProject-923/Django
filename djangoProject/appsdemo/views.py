import django.http
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

def get_users(request):
    # 获取所有用户数据
    users = Users.objects.all().values('id', 'name', 'phone', 'size', 'text1')  # values 可以限制字段

    # 将查询结果转为字典列表
    users_list = list(users)

    return JsonResponse(users_list, safe=False)  # 返回 JSON 格式

def get_migrations(request):
    # 获取所有迁移数据
    django_migrations = Migrations.objects.all().values('id','app', 'name')  # values 可以限制字段

    # 将查询结果转为字典列表
    migrations_list = list(django_migrations)

    return JsonResponse(migrations_list, safe=False)  # 返回 JSON 格式

@csrf_exempt
def update_users(request):
    if request.method == "POST":
        try:
            # 获取 POST 数据
            user_id = request.POST.get('id')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            size = request.POST.get('size')

            # 获取用户实例
            user = Users.objects.get(id=user_id)

            # 调用实例方法更新用户信息
            user.update_users(name=name, phone=phone, size=size)

            return JsonResponse({'message': 'User updated successfully', 'user_id': user.id}, status=200)
        except Users.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=404)  # 404 - 用户不存在
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)  # 405 - 请求方法不允许
