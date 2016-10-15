from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'register/index.html')


def register(request):
    # Create a dummie user to save [WIP]
    user = ['one', 'two', 'three']
    example = {
        "my": "son",
        "you": "are",
        "awesome": "people"
    }
    return render(request, 'home/register.html', {'user': user, 'example': example})
