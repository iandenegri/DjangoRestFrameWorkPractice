# from django.views.generic import View
import json
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import StatusSerializer
from status.models import Status


def is_json(json_data):
    try:
        real_json=json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


# The end all be all View. Does everything.
class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = StatusSerializer
    passed_id               = None

    def get_queryset(self):
        request = self.request
        QuerySet = Status.objects.all()
        query = request.GET.get('q') #q stands for query
        if query is not None:
            QuerySet = QuerySet.filter(content__icontains=query)
        return QuerySet

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        QuerySet = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(QuerySet, id = passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id

        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        requested_id = request.data.get('id')
        passed_id = url_passed_id or new_passed_id or requested_id or None
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)


    # Currently the destroy function doesn't destroy objects that don't exist. It should just pass or return none.
    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)

#####################################################










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


# CreateModelMixin -- Post Data
# UpdateModelMixin -- Put Data
# DestroyModelMixin -- Delete data
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     serializer_class        = StatusSerializer

# Change the end of the URL to look like: http://127.0.0.1:8000/api/status/?q=<search query would go here>
    # def get_queryset(self):
    #     QuerySet = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         QuerySet = QuerySet.filter(content__icontains=query)
    #     return QuerySet
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


#################


# This view is no longer needed. The list view can handle API creation with The
# mixin that's been added.

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# # Change the end of the URL to look like: http://127.0.0.1:8000/api/status/?q=<search query would go here>
#     def get_queryset(self):
#         QuerySet = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             QuerySet = QuerySet.filter(content__icontains=query)
#         return QuerySet


#################


# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

# The class below does the same as the class above but with only one call.

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



##################


# Views below are no longer needed due to mixings filling in their original
# Intended fuctionality. :-)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'
#
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'
