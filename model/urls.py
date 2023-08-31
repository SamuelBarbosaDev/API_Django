from django.urls import path
from model.api.viewsets import (
    model_api
)


urlpatterns = [
    path('', model_api),
]
