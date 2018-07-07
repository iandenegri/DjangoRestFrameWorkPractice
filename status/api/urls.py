from django.urls import path, include

from .views import StatusAPIView

urlpatterns = [
    path('',StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.asview()),
    # path('<int:id>/',StatusDetailAPIView.as_view()),
    # path('<int:id>/update/',StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/',StatusDeleteAPIView.as_view()),

]
