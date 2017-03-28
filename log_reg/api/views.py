from log_reg.models import User, UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def register(request):
    if request.method == "POST":
        data = request.data
        name = data.get('name')
        passwd = data.get('password')

        # 手机注册用户
        if 'phone' in data:
            phone = data.get('phone')
            user_exist = User.objects.filter(username=phone).exists()
            # 手机号被注册
            if user_exist:
                return Response({'msg': '手机号已被注册'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_info = User(username=phone)
                user_info.set_password(passwd)
                user_info.save()
                UserProfile.objects.create(belong=user_info, name=name, phone=phone)

                return Response({"msg": '注册成功'}, status=status.HTTP_200_OK)

        # 邮箱注册用户
        elif 'email' in data:
            email = data.get('email')
            user_exist = User.objects.filter(username=email).exists()
            # 邮箱被注册
            if user_exist:
                return Response({'msg': '邮箱已被注册'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_info = User(username=email)
                user_info.set_password(passwd)
                user_info.save()
                UserProfile.objects.create(belong=user_info, name=name, email=email)

                return Response({"msg": '注册成功'}, status=status.HTTP_200_OK)
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == "POST":
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        # 判断用户信息是否正确
        if not user or not username:
            return Response({'msg': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 用户信息正确生成token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def login_or_not(request):
    if request.method == "GET":

        if request.auth:
            request_user = request.user
            data = {
                'username': request_user.username,
                'name': request_user.profile.name
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response({'user': 'Not Login'}, status=status.HTTP_401_UNAUTHORIZED)
