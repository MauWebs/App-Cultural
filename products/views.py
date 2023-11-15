from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
@permission_classes([IsAdminUser])
def postProduct(request):

    data = request.data
    user = request.user

    if request.method == 'POST':

        if user.rol == 'admin':

            new = Product.objects.create(
                user=request.user,
                title=data['title'],
                description=data['description'],
                price=data['price'],
                url=data['url'],
            )

            serializer = ProductSerializer(new, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'ERROR METHOD, USE "POST"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':

            product = Product.objects.get(id=pk)

            product.delete()

            return Response({'message': 'Fue eliminado correctamente'})

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
def getAllProduct(request):

    if request.method == 'GET':

        virtual_reality = Product.objects.all()

        serializer = ProductSerializer(virtual_reality, many=True)

        return Response(serializer.data)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #