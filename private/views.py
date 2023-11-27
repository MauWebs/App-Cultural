from django.core.management import call_command
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create_backup(request):

    try:
        call_command('dbbackup')
        return Response({'mensaje': 'Copia de seguridad creada correctamente'})
    
    except:
        return Response({'mensaje':'La copia de seguridad no se puedo realizar'})