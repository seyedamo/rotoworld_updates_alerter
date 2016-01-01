from django.views.generic.edit import CreateView

from users.models import User
from users.serializers import UserSerializer

from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.


from users.forms import SignUpForm


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


class UserFormCreationView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(SignUpForm, self).form_valid(form)


class UserCreate(CreateView):
    model = User
    fields = ['email_address']