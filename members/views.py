from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializer import MemberSerializer

@api_view(['GET'])
def get_member(request):
    return Response(MemberSerializer({'first_name': 'David', 'last_name': 'Ricaurte'}).data)


