from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response


@api_view()
def model_api(request):
    return Response('Ok')

# Create your views here.
