from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Serverhosts, Fixedassets
from .serializers import UserSerializer, ServerhostsSerializer, FixedassetsSerializer


# 获取所有用户或创建新用户
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 获取、更新或删除单个用户
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response({'message': '用户删除成功'}, status=status.HTTP_204_NO_CONTENT)

# 获取所有服务主机和新增主机
@api_view(['GET', 'POST'])
def serverhosts_list(request):
    if request.method == 'GET':
        serverhosts = Serverhosts.objects.all()
        serializer = ServerhostsSerializer(serverhosts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServerhostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 获取、更新或删除单个服务主机
@api_view(['GET', 'PUT', 'DELETE'])
def serverhost_detail(request, serverhost_id):
    try:
        serverhost = Serverhosts.objects.get(id=serverhost_id)
    except Serverhosts.DoesNotExist:
        return Response({'error': '主机不存在'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServerhostsSerializer(serverhost)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ServerhostsSerializer(serverhost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        serverhost.delete()
        return Response({'message': '主机删除成功'}, status=status.HTTP_204_NO_CONTENT)


# 获取/新增所有固定资产清单
@api_view(['GET', 'POST'])
def fixedassets_list(request):
    if request.method == 'GET':
        fixedassets = Fixedassets.objects.all()
        serializer = FixedassetsSerializer(fixedassets, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FixedassetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 获取、更新或删除单个固定资产
@api_view(['GET', 'PUT', 'DELETE'])
def fixedassets_detail(request, fixed_asset_id):
    try:
        fixedasset = Serverhosts.objects.get(id=fixed_asset_id)
    except Serverhosts.DoesNotExist:
        return Response({'error': '资产不存在'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fixedasset = Fixedassets.objects.get(id=fixed_asset_id)
        serializer = FixedassetsSerializer(fixedasset, many=True)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        serializer = FixedassetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        fixedasset.delete()
        return Response({'message': '资产数据删除成功'}, status=status.HTTP_204_NO_CONTENT)
