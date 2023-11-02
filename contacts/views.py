from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Contacts
from .serializers import ContactsSerializer

# --------------------------------------------------------------------------- #


@api_view(['POST'])
def postContact(request):

    if request.method == 'POST':
        
        data = request.data
        web = data.get('web', None)

        contact = Contacts.objects.create(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            web=web,
            matter=data['matter'],
            consultation=data['consultation'],
            message=data['message'],
        )

        serializer = ContactsSerializer(contact, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response({'error':'ERROR METHOD, USE "POST"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes({IsAuthenticated})
def getAllContact(request):

    user = request.user
    
    if request.method == 'GET':
    
        if user.rol == 'editor' or user.rol == 'admin':
            
            contact = Contacts.objects.all()
        
            serializer = ContactsSerializer(contact, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        return Response({'error':'ERROR METHOD, USE "GET"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# --------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes({IsAuthenticated})
def getIdContact(request, pk):

    user = request.user

    if request.method == 'GET':

        if user.rol == 'editor' or user.rol == 'admin':
                
            contact = Contacts.objects.get(id=pk)
            
            serializer = ContactsSerializer(contact, many=False)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
    else:
        return Response({'error':'ERROR METHOD, USE "GET"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

# --------------------------------------------------------------------------- #

@api_view(['DELETE'])
@permission_classes({IsAdminUser})
def deleteIdContact(request, pk):

    user = request.user

    if request.method == 'DELETE':

        if user.rol == 'admin':
                
            contact = Contacts.objects.get(id=pk)
            
            contact.delete()
            
            return Response({"message": "Eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response({'error': 'No tienes permisos para eliminar contactos'}, status=status.HTTP_403_FORBIDDEN)
    
    else:
        return Response({'error':'ERROR METHOD, USE "DELETE"'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

# --------------------------------------------------------------------------- #