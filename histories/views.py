from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import History
from .serializers import HistorySerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postHistory(request):

    data = request.data

    digital = History.objects.create(
        user=request.user,
        title=data['title'],
        description=data['description'],
        format=data['format'],
        tag=data['tag'],
        url=data['url'],
    )

    serializer = HistorySerializer(digital, many=False)
    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteHistory(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':

            try:
                digital_object = History.objects.get(id=pk)
                digital_object.delete()
                return Response({'message': 'Fue eliminado correctamente'})

            except History.DoesNotExist:
                return Response({'message': 'El objeto no existe'}, status=status.HTTP_404_NOT_FOUND)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllHistory(request):

    digital = History.objects.all()

    serializer = HistorySerializer(digital, many=True)

    return Response(serializer.data)


# --------------------------------------------------------------------------- #