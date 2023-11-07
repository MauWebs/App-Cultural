from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Suggestions
from .serializers import SuggestionsSerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
def postSuggestion(request):

    data = request.data

    suggestion =Suggestions.objects.create(
        description = data['description']
    )

    serializer = SuggestionsSerializer(suggestion, many=False)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllSuggestions(request):

    suggestion =Suggestions.objects.all()

    serializer = SuggestionsSerializer(suggestion, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getSuggestion(request, pk):

    try:
      
        suggestion = Suggestions.objects.get(id=pk)
        serializer = SuggestionsSerializer(suggestion, many=False)
       
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Suggestions.DoesNotExist:
       
        return Response({"error": "La sugerencia no existe"}, status=status.HTTP_404_NOT_FOUND)


# --------------------------------------------------------------------------- #