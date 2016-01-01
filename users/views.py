from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import FormView

from users.models import User

# Create your views here.


from users.forms import SubscriptionForm


def signup(request):
    if request.method == 'GET':
        form = SubscriptionForm()
        return render(request, 'signup.html', {'form': form})


def unsubscribe(request):
    if request.method == 'GET':
        form = SubscriptionForm()
        return render(request, 'unsubscribe.html', {'form': form})


def thanks(request):
    if request.method == 'GET':
        return render(request, 'thanks.html')


def goodbye(request):
    if request.method == 'GET':
        return render(request, 'goodbye.html')


class UserFormCreationView(FormView):
    template_name = 'signup.html'
    form_class = SubscriptionForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(SubscriptionForm, self).form_valid(form)


class UnsubscribeFormView(FormView):
    template_name = 'unsubscribe.html'
    form_class = SubscriptionForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(SubscriptionForm, self).form_valid(form)


class UserCreate(CreateView):
    model = User
    fields = ['email_address']


class UserUnsubscribe(DeleteView):
    model = User
    fields = ['email_address']