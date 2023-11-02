from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import News
from .serializers import NewSerialaizer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postNew(request):

    data = request.data
    user = request.user

    if request.method == 'POST':

        if user.rol == 'admin':

            new = News.objects.create(
                user=request.user,
                title=data['title'],
                url=data['url'],
                description=data['description'],
            )

            serializer = NewSerialaizer(new, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'ERROR METHOD, USE "POST"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def putNew(request, pk):

    data = request.data
    user = request.user

    if request.method == 'PUT':

        if user.rol == 'admin' or user.rol == 'editor':

            news = News.objects.get(id=pk)
            news.title = data.get('title', news.title)
            news.url = data.get('url', news.url)
            news.description = data.get('description', news.description)
            news.save()

            serializer = NewSerialaizer(news, many=False)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        return Response({'error': 'ERROR METHOD, USE "PUT"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteNew(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':

            news = News.objects.get(id=pk)

            news.delete()

            return Response({'message': 'Noticia Eliminada correctamente'}, status=status.HTTP_202_ACCEPTED)

    else:
        return Response({'error': 'ERROR METHOD, USE "DELETE"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllNews(request):

    if request.method == 'GET':

        news = News.objects.all()

        serializer = NewSerialaizer(news, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'ERROR METHOD, USE "GET"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getIdNew(request, pk):

    if request.method == 'GET':

        new = News.objects.get(id=pk)

        serializer = NewSerialaizer(new, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'ERROR METHOD, USE "GET"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #
