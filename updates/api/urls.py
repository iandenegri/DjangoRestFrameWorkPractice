from django.urls import path
from .views import (UpdateModelListAPIView,
                    UpdateModelDetailAPIView)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view(), name='DetailListView'), #view a list of all the objects
    path('<int:id>/', UpdateModelDetailAPIView.as_view(), name='cbv'),
]
