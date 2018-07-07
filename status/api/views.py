# from django.views.generic import View
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StatusSerializer
from status.models import Status

# class StatusListSearchAPIView(APIView):
#     permission_classes      = []
#     authentication_classes  = []
#
#     def get(self, request, format=None):
#         QuerySet = Status.objects.all()
#         serialized_data = StatusSerializer(QuerySet, many=True)
#         return Response(serialized_data.data)
#
#     def post(self,request,format=None):
#         QuerySet = Status.objects.all()
#         serialized_data = StatusSerializer(QuerySet, many=True)
#         return Response(serialized_data.data)

class StatusAPIView(generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = StatusSerializer

# Change the end of the URL to look like: http://127.0.0.1:8000/api/status/?q=<search query would go here>
    def get_queryset(self):
        QuerySet = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            QuerySet = QuerySet.filter(content__icontains=query)
        return QuerySet
