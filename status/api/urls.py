from django.urls import path, include

from .views import (StatusAPIView,
                    # StatusCreateAPIView,
                    # StatusDetailAPIView,
                    # StatusUpdateAPIView,
                    # StatusDeleteAPIView
                    )

urlpatterns = [
    path('',StatusAPIView.as_view()),
    # Outdated due to adding a create section in the list view. :-)
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:id>/',StatusDetailAPIView.as_view()),
    # Detail view can do updates and deletes now. :-D
    # path('<int:id>/update/',StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/',StatusDeleteAPIView.as_view()),

]
