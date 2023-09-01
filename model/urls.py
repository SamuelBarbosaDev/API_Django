from django.urls import path
from rest_framework import routers
from model.api.viewsets import (
    model_api,
    prediction,
    multiple_predictions,
    mult_predict_wiht_csv,
    CSVPredictionView
)

route = routers.DefaultRouter()
route.register(r'model/', model_api, basename='model')

urlpatterns = [
    path('', model_api),
    path('prediction', prediction),
    path('multiple_predictions', multiple_predictions),
    # path('mult_predict_wiht_csv', mult_predict_wiht_csv),
    path('prediction_with_csv', CSVPredictionView.as_view()),
]
