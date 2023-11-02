from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializers = UserSerializerWithToken(self.user).data

        for token, user in serializers.items():
            data[token] = user

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# --------------------------------------------------------------------------- #


@api_view(['POST'])
def register(request):
    data = request.data
    try:

        existing_user = User.objects.filter(email=data['email']).first()
        if existing_user:
            message = {'detail': 'El correo electrónico ya está registrado.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
        data['rol'] = 'user'
        user = User.objects.create(
            user_name=data['user_name'],
            last_name=data['last_name'],
            email=data['email'],
            rol=data['rol'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Algo salió mal'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------------------- #


@api_view(['POST'])
def registerAdmin(request):
    data = request.data
    try:

        existing_user = User.objects.filter(email=data['email']).first()
        if existing_user:
            message = {'detail': 'El correo electrónico ya está registrado.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
        data['rol'] = 'admin'
        data['is_staff'] = True
        user = User.objects.create(
            user_name=data['user_name'],
            last_name=data['last_name'],
            email=data['email'],
            rol=data['rol'],
            is_staff=data['is_staff'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Algo salió mal'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------------------- #


@api_view(['POST'])
def registerEditor(request):
    data = request.data
    try:

        existing_user = User.objects.filter(email=data['email']).first()
        if existing_user:
            message = {'detail': 'El correo electrónico ya está registrado.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        data['rol'] = 'editor'
        user = User.objects.create(
            user_name=data['user_name'],
            last_name=data['last_name'],
            email=data['email'],
            rol=data['rol'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Algo salió mal'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

# --------------------------------------------------------------------------- #


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def putUser(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.user_name = data['user_name']
    user.email = data['email']
    if data['password'] != '':
        user.password = make_password(data['password'])
    user.save()
    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSoloUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# --------------------------------------------------------------------------- #