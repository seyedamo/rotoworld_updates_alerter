from users.models import User
from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'users/signup.html')


class UserCreationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer