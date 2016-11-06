from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views import generic
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route

from .serializers import CustomerSerializer
from .models import Customer


class RegisterView(generic.ListView):
    template_name = 'register/index.html'
    # TO-DO:
    # context_object_name = 'latest_advertisements'
    pass


class DetailView(generic.ListView):
    template_name = 'register/register.html'


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer

    def create(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                customer = serializer.save()
            except Exception as e:
                raise
            return Response(serializer.data, status=201)

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)



@api_view(['GET'])
def activate_user_view(request, id):
    # result = activate_user(id)
    result = "Ola k ase"
    return Response(result, 200)
