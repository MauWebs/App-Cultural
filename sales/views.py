from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Sales
from .serializers import SalesSerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postSales(request):

    if request.method == 'POST':

        data = request.data

        sale = Sales.objects.create(
            user=request.user,
            products=data['products'],
            total_amount=data['total_amount']
        )

        serializer = SalesSerializer(sale, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'ERROR METHOD, USE "POST"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSales(request):

    if request.method == 'GET':

        data = request.data

        sale = Sales.objects.all()

        serializer = SalesSerializer(sale, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        return Response({'error': 'ERROR METHOD, USE "GET"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #
