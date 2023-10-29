from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Comment, DigitalObject, Rating
from .serializers import (CommentSerializer, DigitalObjectSerializer,
                          RatingSerializer)

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllDigitalObjects(request):
    
    digital = DigitalObject.objects.all()

    serializer = DigitalObjectSerializer(digital, many=True)

    for digital_obj in serializer.data:
        ratings = Rating.objects.filter(digital_object_id=digital_obj['id'])
        rating_serializer = RatingSerializer(ratings, many=True)
        digital_obj['ratings'] = rating_serializer.data

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getIdDigitalObjects(request, pk):
    
    try:

        digital = DigitalObject.objects.get(id=pk)
        serializer = DigitalObjectSerializer(digital)
        return Response(serializer.data)

    except DigitalObject.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


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
                rating = Rating.objects.get(user=user, digital_object=digital_object)
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
    if request.method == 'POST':
        try:
            digital_object = DigitalObject.objects.get(pk=pk)
        except DigitalObject.DoesNotExist:
            return Response({"detail": "DigitalObject no encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(digital_object=digital_object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)