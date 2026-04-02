from rest_framework.viewsets import ModelViewSet
from .models import User 
from .serializers import UserSerializer
from .permissions import IsAdmin

# Create your views here.

class UserViewSet(ModelViewSet):
          queryset = User.objects.all()
          serailizer_class = UserSerializer
          permission_classes = [IsAdmin]
