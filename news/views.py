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
                title = data['title'],
                url = data['url'],
                description = data['description'],
            )

            serializer = NewSerialaizer(new, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'ERROR METHOD, USE "POST"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# --------------------------------------------------------------------------- #
