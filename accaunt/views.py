from main.models import User
from main.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from .tookens import *


"""  User log in model  """
@api_view(['POST'])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                token = get_tokens_for_user(usr)
                status = 200
                date = {
                    'status': status,
                    'username': username,
                    'token': token
                }
            else:
                status = 403
                message = "Invalid Password or Username"
                date = {
                    'status': status,
                    'message': message
                }
        except User.Doesnotexist:
            status = 404
            message = "this User is not defined"
            date = {
                'status': status,
                'message': message
            }
        return Response(date)
    except Exception as err:
        return Response(f'{err}')


"""  User register model  """
@api_view(['POST'])
def sang_up_view(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        new = User.objects.create_user(
            username=username,
            password=password,
            age=age,
            phone_number=phone_number,
            email=email,
        )
        ser = UserSerializer(new)
        return Response(ser.data)
    except Exception as err:
        return Response(f'{err}')


"""  User log out model  """
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'date': 'sucses'})


"""  User update model  """
@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST['username']
            password = request.POST['password']
            age = request.POST['age']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            user.username = username
            user.age = age
            user.phone_number = phone_number
            user.email = email
            if password is not None:
                user.set_password(password)
                user.save()
            ser = UserSerializer(user)
            return Response(ser.data)
        except:
            status = 404
            message = "Request failed"
            date = {
                'status': status,
                'message': message
            }
            return Response(date)
    except:
        status = 404
        message = "User not found"
        date = {
            'status': status,
            'message': message
        }
        return Response(date)



"""  User delete model  """
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        date = {
            'message': "User deleted successfully"
        }
    except:
        status = 404
        message = "User nod found"
        date = {
            'status': status,
            'message': message
        }
    return Response(date)
