from users.models import User
from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer

# Create your views here.


class UserCreationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer