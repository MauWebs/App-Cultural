from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from users.models import User

from .models import Comment, DigitalObject, Rating
from .serializers import (CommentSerializer, DigitalObjectSerializer,
                          RatingSerializer)

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postDigitalObject(request):

    data = request.data

    digital = DigitalObject.objects.create(
        user=request.user,
        title=data['title'],
        description=data['description'],
        place=data['place'],
        format=data['format'],
        tag=data['tag'],
        url=data['url'],
    )

    serializer = DigitalObjectSerializer(digital, many=False)
    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllDigitalObjects(request):

    digital = DigitalObject.objects.all()

    serializer = DigitalObjectSerializer(digital, many=True)

    for digital_obj in serializer.data:
        ratings = Rating.objects.filter(digital_object_id=digital_obj['id'])
        rating_serializer = RatingSerializer(ratings, many=True)
        digital_obj['ratings'] = rating_serializer.data

    return Response(serializer.data)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getIdDigitalObjects(request, pk):

    try:

        digital = DigitalObject.objects.get(id=pk)
        serializer = DigitalObjectSerializer(digital)
        return Response(serializer.data)

    except DigitalObject.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


# --------------------------------------------------------------------------- #


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def putDigitalObject(request, pk):

    data = request.data
    user = request.user

    try:
        digital = DigitalObject.objects.get(id=pk)
    except DigitalObject.DoesNotExist:
        return Response({"detail": "El objeto digital no existe"}, status=404)

    if user.rol == 'editor' or user.rol == 'admin':
        digital.title = data.get('title', digital.title)
        digital.description = data.get('description', digital.description)
        digital.place = data.get('place', digital.place)
        digital.format = data.get('format', digital.format)
        digital.tag = data.get('tag', digital.tag)
        digital.url = data.get('url', digital.url)
        digital.save()

        serializer = DigitalObjectSerializer(digital, many=False)
        return Response(serializer.data)

    else:
        return Response({"detail": "No tienes permiso para actualizar objetos digitales"}, status=403)


# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postRating(request, pk):

    try:

        digital_object = DigitalObject.objects.get(id=pk)
        user = request.user
        rating_value = request.data.get('rating_value')

        if 1 <= rating_value <= 5:
            try:
                rating = Rating.objects.get(
                    user=user, digital_object=digital_object)
                rating.rating_value = rating_value
                rating.save()
            except Rating.DoesNotExist:
                rating = Rating.objects.create(
                    user=user,
                    digital_object=digital_object,
                    rating_value=rating_value
                )

            serializer = RatingSerializer(rating)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response({"error": "El valor de la calificación debe estar entre 1 y 5"}, status=status.HTTP_BAD_REQUEST)

    except DigitalObject.DoesNotExist:
        return Response({"error": "El objeto digital no existe"}, status=status.HTTP_NOT_FOUND)


# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postComment(request, pk):

    data = request.data
    digital_object = DigitalObject.objects.get(id=pk)
    user = request.user

    if 'description' in data:
       
        comment_description = data['description']

        comment_data = {
            'user': user.id,
            'description': comment_description,
            'digital_object': digital_object.id
        }

        serializer = CommentSerializer(data=comment_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"error": serializer.errors}, status=400)
    
    else:
        return Response({"error": "El campo 'description' es obligatorio en los datos del comentario."}, status=400)


# --------------------------------------------------------------------------- #