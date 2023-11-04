from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import VirtualReality
from .serializers import VirtualRealitySerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postImage(request):

    user = request.user

    if request.method == 'POST':

        if user.rol == 'admin':

            serializer = VirtualRealitySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:

            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 


# --------------------------------------------------------------------------- #