from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from masterdata.serializers import *


class ListRoles(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, arg):
        try:
            roles = Role.objects.all().order_by('name')
            serializer = RoleSerializer(roles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': repr(e)}, status=status.HTTP_400_BAD_REQUEST)