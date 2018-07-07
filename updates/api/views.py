from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin
import json

# This can update, delete, and retrieve 1 object

'''
Retrieve, update and delete an object/detail
'''

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json=True

    def get(self,request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize_single()
        return self.render_to_response(data=json_data)

    def put(self, request, *args, **kwargs):
        json_data=json.dumps({'Weh':'He told me oo ee oo ah ah'})
        return self.render_to_response(data=json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'Error':'There is not really an error, this is just placeholder.'})
        return self.render_to_response(data=json_data, status=403)

###########################

'''
List view and create view
'''
class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        queryset = UpdateModel.objects.all()
        json_data = queryset.serialize_set()
        return HttpResponse(json_data, content_type='application/json')#, status_code=status)


    def post(self, request, *args, **kwargs):
        print(request.POST)
        json_data = json.dumps({'message':'unknown'})
        return HttpResponse(json_data, content_type='application/json')#, status_code=status)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'Error':'You can not delete the entire list.'})
        return HttpResponse(json_data, content_type='application/json')#, status_code=status)
