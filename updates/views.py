from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.views.generic import View
from .models import Update
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize

##########################

def json_example_view(request):
    '''
    URI foundation being built for a REST API
    GET - Retrieving data via view.
    '''
    data = {
        "count":1000,
        "content":"Some content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

##########################

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":1000,
            "content":"Some content"
        }
        return JsonResponse(data)

##########################

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count":1000,
            "content":"Some content"
        }
        return self.render_to_json_response(data)

################

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = obj.serialize_single()

        # Code below is no longer necessary and is just a complicated way of
        # doing the code above

        # data = serialize('json', [obj,], fields=('user','content'))
        # data = {
        #     "user":obj.user.username,
        #     "content":obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')

####################

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()

        # Code below is no longer necessary and is just a complicated way of
        # doing the code above

        # data = serialize('json', qs, fields=('user','content'))
        # data = {
        #     "user":obj.user.username,
        #     "content":obj.content
        # }
        # json_data = json.dumps(data)

        data = Update.objects.all().serialize_set()
        return HttpResponse(data, content_type='application/json')
