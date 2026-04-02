from rest_framework.viewsets import ModelViewSet
from .models import Record
from . serializers import RecordSerializer
from rest_framework.response import Response
from .services import get_summary
from apps.users.permissions import IsAnalystOrAdmin



class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAnalystOrAdmin]



from rest_framework.views import APIView


class DashboardView(APIView):
    permission_classes = [IsAnalystOrAdmin]

    def get(self, request):
        return Response(get_summary())