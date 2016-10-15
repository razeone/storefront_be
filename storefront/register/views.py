from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.utils import timezone


class RegisterView(generic.ListView):
    template_name = 'register/index.html'
    # TO-DO:
    # context_object_name = 'latest_advertisements'
    pass


class DetailView(generic.ListView):
    template_name = 'register/register.html'


def register(request):
    # Create a dummie user to save [WIP]
    user = ['one', 'two', 'three']
    example = {
        "my": "son",
        "you": "are",
        "awesome": "people"
    }
    return render(request, 'register/register.html', {'user': user, 'example': example})
