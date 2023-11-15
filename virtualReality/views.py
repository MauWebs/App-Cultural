from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from virtualReality.models import VirtualReality

from .serializers import VirtualRealitySerializer

# --------------------------------------------------------------------------- #


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def uploadImage(request, pk):
   
    try:
        user = VirtualReality.objects.get(id=pk)
   
    except VirtualReality.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method in ['POST', 'PUT']:
   
        if 'image' in request.FILES:
   
            user.image = request.FILES['image']
            user.save()
            serializer = VirtualRealitySerializer(user)
            return Response({'message': 'Imagen subida exitosamente', 'user_data': serializer.data})
   
        else:
            return Response({'error': 'No se proporcionó ninguna imagen'}, status=status.HTTP_400_BAD_REQUEST)
   
    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postVirtualReality(request):
    data = request.data

    if request.method == 'POST':

        virtual_reality = VirtualReality.objects.create(
            user=request.user,
            title=data['title'],
            description=data['description'],
            place=data['place'],
            format=data['format'],
            tag=data['tag'],
            url=data['url']
        )

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
