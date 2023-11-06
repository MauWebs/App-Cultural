import os
from uuid import uuid4

from django.conf import settings
from django.core.files.storage import default_storage
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

    if request.method == 'POST':

        serializer = VirtualRealitySerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            uploaded_image = request.FILES.get('img')
            
            if uploaded_image:
                image_path = save_uploaded_image(uploaded_image)
                serializer.validated_data['img'] = image_path
            
            VirtualReality.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                place=serializer.validated_data['place'],
                format=serializer.validated_data['format'],
                tag=serializer.validated_data['tag'],
                image=serializer.validated_data['img'] 
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------------------- #


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteVirtualReality(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':

            VirtualReality.object.delete(id=pk)

            return Response({'message':'Fue eliminado correctamente'})

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 


# --------------------------------------------------------------------------- #

