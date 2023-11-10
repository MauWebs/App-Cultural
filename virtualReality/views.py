import os
from uuid import uuid4

from django.conf import settings
from django.core.files.storage import default_storage
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from virtualReality.models import VirtualReality

from .serializers import VirtualRealitySerializer

# --------------------------------------------------------------------------- #


def save_uploaded_image(uploaded_image):

    unique_filename = f'{str(uuid4())}.{uploaded_image.name.split(".")[-1]}'
    image_path = os.path.join(settings.MEDIA_ROOT, 'media', unique_filename)

    with default_storage.open(image_path, 'wb') as destination:
        for chunk in uploaded_image.chunks():
            destination.write(chunk)

    return os.path.join('media', unique_filename)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postVirtualReality(request):
    data = request.data

    if request.method == 'POST':

        uploaded_image = request.FILES.get('img')

        if uploaded_image:
            virtual_reality = VirtualReality.objects.create(
                user=request.user,
                title=data['title'],
                description=data['description'],
                place=data['place'],
                format=data['format'],
                tag=data['tag'],
                image=data['img'],
                url=data['url']
            )

            image_path = save_uploaded_image(uploaded_image)

            virtual_reality.img = image_path
            
            virtual_reality.save()

            serializer = VirtualRealitySerializer(virtual_reality, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------------------- #


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteVirtualReality(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':

            virtual_reality = VirtualReality.objects.get(id=pk)

            virtual_reality.delete()

            return Response({'message': 'Fue eliminado correctamente'})

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllVirtualReality(request):

    if request.method == 'GET':

        virtual_reality = VirtualReality.objects.all()

        serializer = VirtualRealitySerializer(virtual_reality, many=True)

        return Response(serializer.data)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getIdVirtualReality(request, pk):

    if request.method == 'GET':

        virtual_reality = VirtualReality.objects.get(id=pk)

        serializer = VirtualRealitySerializer(virtual_reality, many=False)

        return Response(serializer.data)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #
