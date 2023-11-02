from rest_framework import status
from rest_framework.decorators import api_view
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